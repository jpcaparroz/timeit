from datetime import datetime
from typing import Optional

from ..utils import get_env


DATE_FORMAT: str = get_env('NOTION_DATE_FORMAT_TIMEIT')
DATABASE_ID: str = get_env('NOTION_DATABASE_TIMEIT_ID')


class Timeit():
    """TimeiT notion class representation
    """

    def __init__(self,
                 tag: str,
                 description: str,
                 project: str,
                 time: float,
                 date: Optional[datetime] = None) -> None:
        
        self.database_id = DATABASE_ID
        self.tag = tag
        self.description = description
        self.project = project
        self.time = time
        self.date = date if date else datetime.now().strftime(DATE_FORMAT)


    def to_dict(self) -> dict:
        body_as_dict: dict = {
            'DatabaseId': self.database_id,
            'Tag': self.tag,
            'Description': self.description,
            'Project': self.project,
            'Time': self.time,
            'Date': self.date
        }
        
        return body_as_dict


    def get_parent(self) -> dict:
        """Get notion parent expect json

        Returns:
            dict: Notion body properties to post a page
        """
        parent: dict = {
            "type": "database_id", 
            "database_id": self.database_id
        }
    
        return parent


    def notion_api_json(self) -> dict:
        """Get notion expect json

        Returns:
            dict: Notion json to post a page
        """
        body_json: dict = {
                        "tag": {
                            "rich_text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": self.tag,
                                        "link": None
                                    },
                                    "annotations": {
                                        "bold": False,
                                        "italic": False,
                                        "strikethrough": False,
                                        "underline": False,
                                        "code": False,
                                        "color": "default"
                                    },
                                    "plain_text": self.tag,
                                    "href": None
                                }
                            ]
                        },
                        "description": {
                            "id": "description",
                            "type": "title",
                            "title": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": self.description,
                                        "link": None
                                    },
                                    "annotations": {
                                        "bold": False,
                                        "italic": False,
                                        "strikethrough": False,
                                        "underline": False,
                                        "code": False,
                                        "color": "default",
                                    },
                                    "plain_text": self.description,
                                    "href": None,
                                }
                            ],
                        },
                        "project": {
                            "type": "select",
                            "select": {
                                "name": self.project,
                            }
                        },
                        "time": {
                            "type": "number",
                            "number": self.time
                        },
                        "date": {
                            "type": "date",
                            "date": {
                                "start": self.date,
                                "end": None,
                                "time_zone": None 
                            }
                        }
                    }

        return body_json