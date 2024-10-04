from enum import StrEnum


class DateInfo(StrEnum):
    today_release = 'Post today time release'
    custom_date_release = 'Post custom date release (yyyy-mm-dd)'


class ClearPage(StrEnum):
    delete_pages = 'Delete pages after post it'
    not_delete_pages = 'No delete pages after post it'


class ParameterInputTypes(StrEnum):
    custom_date = 'Type the custom date (yyyy-mm-dd):'
