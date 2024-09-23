from notion_client import AsyncClient

from ..utils import get_env


class TNotion():
    """TNotion notion class representation
    """

    def __init__(self) -> None:
        self.api_key = get_env('NOTION_API_TOKEN')


    async def get_client(self) -> AsyncClient:
        return AsyncClient(auth=self.api_key)
