from notion.client import NotionClient


class TNotion():
    """TNotion notion class representation
    """

    def __init__(self,
                 api_key: str) -> None:
        
        self.api_key = api_key


    def get_client(self) -> NotionClient:
        return NotionClient(self.api_key)
