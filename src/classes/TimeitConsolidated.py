from datetime import datetime
from typing import Optional
from typing import List

from ..utils import get_env
from .Excepts import InvalidTimeitData


DATE_FORMAT: str = get_env('NOTION_DATE_FORMAT_TIMEIT_CONSOLIDATED')
DATABASE_ID: str = get_env('NOTION_DATABASE_TIMEIT_CONSOLIDATED_ID')


class TimeitConsolidated():
    """Timeit Consolidated notion class representation
    """

    def __init__(self,
                 description: str,
                 tags: list,
                 project: str,
                 time: float,
                 date: Optional[datetime] = None) -> None:
        
        self.database_id = DATABASE_ID
        self.description = description
        self.tags = tags
        self.project = project
        self.time = time
        self.date = date if date else datetime.now().strftime(DATE_FORMAT)


    def to_dict(self) -> dict:
        body_as_dict: dict = {
            'DatabaseId': self.database_id,
            'Tags': self.tags,
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
                        "tags": {
                            "multi_select":[
                                {"name": tag} for tag in self.tags
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


def get_consolidated_title(class_list):
    """
    Generates a consolidated title string by formatting the 'tag', 'description', 
    and 'time' attributes of each class in the provided class_list.

    Args:
        class_list (List): A list of class objects where each object contains 
                        'tag', 'description', and 'time' attributes.

    Returns:
        str: A consolidated string where each class is represented as "[tag] description (time)", 
            with entries separated by " / ".
    """
    formatted_strings = []

    for cls in class_list:
        tag = cls.tag
        description = cls.description
        time = str(cls.time)
        treated_time = f'{time},0' if len(time) == 1 else time.replace('.', ',')

        # Format the string
        formatted_string = f"[{tag}] {description} ({treated_time})"
        formatted_strings.append(formatted_string)

    return ' / '.join(formatted_strings)
