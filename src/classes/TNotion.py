from collections import defaultdict
from datetime import datetime
from typing import Optional
from typing import Literal
from typing import List

from notion_client import AsyncClient

from ..utils import get_env
from ..utils import add_log
from . import TimeitConsolidated
from . import get_consolidated_title
from . import get_short_title
from . import TimeitHistorical
from . import create_timeit_historical_from_json
from . import InvalidTimeitData


API_KEY: str = get_env('NOTION_API_TOKEN')
TIMEIT_DATABASE_ID: str = get_env('NOTION_DATABASE_TIMEIT_ID')
DATE_FORMAT_TIMEIT: str = get_env('NOTION_DATE_FORMAT_TIMEIT')
TIMEIT_HISTORICAL_DATABASE_ID: str = get_env('NOTION_DATABASE_TIMEIT_HISTORICAL_ID')


class TNotion():
    """TNotion notion class representation
    """

    def __init__(self) -> None:
        self.client = AsyncClient(auth=API_KEY)
    
    
    async def get_database_page_ids(self, database: Literal['timeit', 'timeit_historical'], date: str) -> List[str]:
        """Get all ID's of a TimeiT database in notion

        Args:
            database (Literal['timeit', 'timeit_historical']): TimeiT default or Historical

        Returns:
            List[str]: A list with all pages id inside database
        """
        
        add_log.info('Getting TimeiT pages ID')
        
        if database == 'timeit':
            database_id: str = TIMEIT_DATABASE_ID
        else:
            database_id: str = TIMEIT_HISTORICAL_DATABASE_ID
            
        query_filter: dict = {
                                "property": "date",
                                "date": {
                                    "equals": date 
                                }
                            }
        
        query: dict = await self.client.databases.query(database_id, filter=query_filter)
        ids: list = [page_id.get('id') for page_id in query.get('results')]
        
        return ids


    async def get_pages(self, database: Literal['timeit', 'timeit_historical'], date: str) -> List[dict]:
        """Get all pages of a TimeiT database in notion

        Args:
            database (Literal['timeit', 'timeit_historical']): TimeiT default or Historical

        Returns:
            List[str]: A list with all pages content inside database
        """
        
        add_log.info('Getting TimeiT pages')
        
        page_ids: list = await self.get_database_page_ids(database, date)
        pages: list = [await self.client.pages.retrieve(page) for page in page_ids]
        
        return pages


    async def post_pages(self, date: str = datetime.now().strftime(DATE_FORMAT_TIMEIT)) -> None:
        
        add_log.info('Initiate post pages on notion processing')
        
        pages: List[dict] = await self.get_pages('timeit', date)
        historical_asset: List[TimeitHistorical] = []
        
        if not pages:
            add_log.error('TimeiT pages not found')
            return None

        for page in pages:
            try:
                historical_asset.append(await create_timeit_historical_from_json(page))
            except InvalidTimeitData as e:
                add_log.error(e)

        # Dictionary to group assets by their 'project' value
        grouped_assets = defaultdict(list)

        add_log.info('Initiate post pages on TimeiT Historical notion database')
        for asset in historical_asset:
            try:
                await self.client.pages.create(parent=asset.get_parent(), 
                                               properties=asset.notion_api_json())
            except Exception as e:
                add_log.error('On TimeiT Historical post')

            grouped_assets[asset.project].append(asset)  # Group assets by 'project'

        add_log.info('Initiate post pages on TimeiT Consolidated notion database')
        for project, assets in grouped_assets.items():
            add_log.info(f'Processing project: {project}')
            
            time_summ: float = 0.0
            title: str = get_consolidated_title(assets)
            short_title: str = get_short_title(assets)
            tags: list = []
            cards: list = []
            print(title)
            print(short_title)
            for asset in assets:
                time_summ += asset.time
                tags.append(asset.tag)
                cards.append(asset.card)
            
            try:
                consolidated = TimeitConsolidated(title, short_title, cards, asset.card, tags, project, time_summ, asset.date)
                await self.client.pages.create(parent=consolidated.get_parent(), 
                                               properties=consolidated.notion_api_json())
            except Exception as e:
                add_log.error('On TimeiT Consolidated post')
