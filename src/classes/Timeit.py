from datetime import datetime

from ..utils import get_env


class Timeit():
    """TimeiT notion class representation
    """

    def __init__(self,
                 tag: str,
                 description: str,
                 project: str,
                 time: float,
                 date: datetime) -> None:
        
        self.database_id = get_env('NOTION_DATABASE_TIMEIT_ID')
        self.tag = tag
        self.description = description
        self.project = project
        self.time = time
        self.date = date


    def to_dict(self) -> str:
        body_as_dict = {
            'DatabaseId': self.database_id,
            'Tag': self.tag,
            'Description': self.description,
            'Project': self.project,
            'Time': self.time,
            'Date': self.date
        }
        
        return body_as_dict


    def notion_api_json(self):
        body_json = {
                        "tag": {
                            "type": "text",
                            "text": {
                                "content": self.tag,
                                "link": None
                            },
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