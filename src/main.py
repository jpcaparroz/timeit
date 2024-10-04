import os

from classes.Types import ConfigType
from classes.Types import ParameterInputTypes
from utils import add_log


"""Entry point for timeit """

def welcome_message() -> None:
    print('--------------------------')
    print('--------- TimeiT ---------')
    print('--------------------------\n')
    print(f'Welcome {os.getlogin()}!\n')


def context_menu() -> ConfigType:
    menu_options = [config_type for config_type in ConfigType]
    
    print('To continue, select one option from below (int):')
    [print(f'{index} - {config_type.value}') for index, config_type 
                                             in enumerate(menu_options)]
    
    selected_index = int(input())
    if selected_index >= len(menu_options) or selected_index < 0:
        raise ValueError("Invalid option selected!")
    
    option_selected = menu_options[selected_index]
    
    return option_selected 


def get_context_menu_variable():
    option_selected: ConfigType = context_menu()
    try:
        if option_selected == ConfigType.today_release:
            pass

        elif option_selected == ConfigType.custom_date_release:
            parameters = [parameter_type for parameter_type in ParameterInputTypes]
            return [str(input(parameter.value)) for parameter in parameters]

    except Exception as e:
        add_log.error(f"Error loading configuration: {e}")


if __name__ == "__main__":
    welcome_message()
    date = get_context_menu_variable()

    print(date)
    pass