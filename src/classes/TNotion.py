from typing import Literal
from typing import List

from notion_client import AsyncClient

from ..utils import get_env


API_KEY: str = get_env('NOTION_API_TOKEN')
TIMEIT_DATABASE_ID: str = get_env('NOTION_DATABASE_TIMEIT_ID')
TIMEIT_HISTORICAL_DATABASE_ID: str = get_env('NOTION_DATABASE_TIMEIT_HISTORICAL_ID')


class TNotion():
    """TNotion notion class representation
    """

    def __init__(self) -> None:
        self.client = AsyncClient(auth=API_KEY)
    
    
    async def get_database_page_ids(self, database: Literal['timeit', 'timeit_historical']) -> List[str]:
        """Get all ID's of a TimeiT database in notion

        Args:
            database (Literal['timeit', 'timeit_historical']): TimeiT default or Historical

        Returns:
            List[str]: A list with all pages id inside database
        """
        if database == 'timeit':
            database_id: str = TIMEIT_DATABASE_ID
        else:
            database_id: str = TIMEIT_HISTORICAL_DATABASE_ID

        query: dict = await self.client.databases.query(database_id)
        ids: list = [page_id.get('id') for page_id in query.get('results')]
        
        return ids


    async def get_pages(self, database: Literal['timeit', 'timeit_historical']) -> List[dict]:
        """Get all pages of a TimeiT database in notion

        Args:
            database (Literal['timeit', 'timeit_historical']): TimeiT default or Historical

        Returns:
            List[str]: A list with all pages content inside database
        """
        page_ids: list = await self.get_database_page_ids(database)
        pages: list = [await self.client.pages.retrieve(page) for page in page_ids]
        
        return pages