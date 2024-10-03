from datetime import datetime
from typing import Optional

from ..utils import get_env
from ..utils import add_log
from .Excepts import InvalidTimeitData


DATE_FORMAT: str = get_env('NOTION_DATE_FORMAT_TIMEIT_HISTORICAL')
DATABASE_ID: str = get_env('NOTION_DATABASE_TIMEIT_HISTORICAL_ID')
NOW_DATE: str = datetime.now().strftime(DATE_FORMAT)


class TimeitHistorical():
    """Timeit Historical notion class representation
    """

    def __init__(self,
                 card: str,
                 tag: str,
                 description: str,
                 project: str,
                 time: float,
                 date: Optional[datetime] = None) -> None:
        
        self.database_id = DATABASE_ID
        self.card = card
        self.tag = tag
        self.description = description
        self.project = project
        self.time = time
        self.date = date if date else NOW_DATE


    def to_dict(self) -> dict:
        body_as_dict: dict = {
            'DatabaseId': self.database_id,
            'Card': self.card,
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
                        "card": {
                            "type": "select",
                            "select": {
                                "name": self.card if self.card else 'none',
                            }
                        },
                        "tag": {
                            "type": "select",
                            "select": {
                                "name": self.tag,
                            }
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


async def create_timeit_historical_from_json(json_content: dict ) -> TimeitHistorical:
    properties: dict = json_content.get('properties', {})

    def get_nested_value(d, *keys):
        for key in keys:
            if isinstance(d, list):
                if not isinstance(key, int) or key >= len(d):
                    return None
                d = d[key]
            elif isinstance(d, dict):
                d = d.get(key)
            else:
                return None
        return d

    card = get_nested_value(properties, 'card', 'select', 'name')
    tag = get_nested_value(properties, 'tag', 'rich_text', 0, 'text', 'content')
    description = get_nested_value(properties, 'description', 'title', 0, 'text', 'content')
    project = get_nested_value(properties, 'project', 'select', 'name')
    time = get_nested_value(properties, 'time', 'number')
    date = get_nested_value(properties, 'date', 'date', 'start')

    # Raise exception if any key value is None or empty
    if not card:
        add_log.warning("Card is missing or empty")
    if not tag:
        add_log.error("Tag is missing or empty")
        raise InvalidTimeitData("Tag is missing or empty")
    if not description:
        add_log.error("Description is missing or empty")
        raise InvalidTimeitData("Description is missing or empty")
    if not project:
        add_log.error("Project is missing or empty")
        raise InvalidTimeitData("Project is missing or empty")
    if time is None or time == 0.0:
        add_log.error("Time is missing or zero")
        raise InvalidTimeitData("Time is missing or zero")
    if not date:
        date = NOW_DATE    

    return TimeitHistorical(card, tag, description, project, time, date)
