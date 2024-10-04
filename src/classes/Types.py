from enum import StrEnum
from enum import Enum


class ConfigType(StrEnum):
    today_release = 'Post today time release'
    custom_date_release = 'Post custom date release (yyyy-mm-dd)'


class ParameterInputTypes(StrEnum):
    custom_date = 'Type the custom date (yyyy-mm-dd):'
