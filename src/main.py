from datetime import datetime
from typing import Literal
import os

from classes.Types import DateInfo
from classes.Types import ClearPage
from classes.Types import ParameterInputTypes
from classes.TNotion import TNotion
from utils import add_log


"""Entry point for timeit """

def welcome_message() -> None:
    print('--------------------------')
    print('--------- TimeiT ---------')
    print('--------------------------\n')
    print(f'Welcome {os.getlogin()}!\n')


def context_menu(custom_menu: Literal['DateInfo', 'ClearPage']):
    if custom_menu == 'DateInfo':
        menu_options = [config_type for config_type in DateInfo]
    else:
        menu_options = [config_type for config_type in ClearPage]
    
    print('To continue, select one option from below (int):')
    [print(f'{index} - {config_type.value}') for index, config_type 
                                             in enumerate(menu_options)]
    
    selected_index = int(input())
    if selected_index >= len(menu_options) or selected_index < 0:
        raise ValueError("Invalid option selected!")
    
    option_selected = menu_options[selected_index]
    
    return option_selected 


def get_context_menu_variable():
    option_selected: DateInfo = context_menu('DateInfo')
    
    result: list = []
    try:
        if option_selected == DateInfo.today_release:
            result.append(None)

        elif option_selected == DateInfo.custom_date_release:
            parameters = [parameter_type for parameter_type in ParameterInputTypes]
            
            for parameter in parameters:
                date = str(input(parameter.value))
                try:
                    datetime.strptime(date, '%Y-%m-%d')
                except Exception as e:
                    add_log.fatal('Invalid date format')
                    raise e
                result.append(date)

        return result[0]

    except Exception as e:
        add_log.error(f"Error loading configuration: {e}")
        raise e


async def main():
    welcome_message()
    date = get_context_menu_variable()
    print('After post pages on historical/consolidated database, what do you want to do?')
    delete_pages = context_menu('ClearPage')

    notion = TNotion()
    await notion.post_pages(date) if date else await notion.post_pages()

    if delete_pages == ClearPage.delete_pages:
        await notion.clear_pages('timeit', date) if date else await notion.clear_pages('timeit')


if __name__ == "__main__":
    import asyncio
    
    asyncio.run(main())
