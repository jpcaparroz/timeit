from configparser import ConfigParser
from datetime import datetime
from pathlib import Path
import logging
import sys
import os

from dotenv import load_dotenv


DEFAULT_SECTION: str = 'TIMEIT'
ENV_PATH = Path(f'{os.getcwd()}/.env')
FORMAT: str = '%(asctime)s  - %(levelname)s - %(message)s'
load_dotenv(dotenv_path=ENV_PATH, override=True)


def get_env(env_name: str) -> str:
    return os.getenv(env_name)


def set_current_directory() -> str:
    """Get current directory of current .py execution

    Returns:
        str: The path
    """

    directory: str = ''
    
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller bundle
        application_path = os.path.dirname(sys.executable)
        directory = os.path.abspath(os.path.join(application_path))
    elif __file__:
        # Running as a standard Python script
        application_path = os.path.dirname(__file__)
        directory = os.path.abspath(os.path.join(application_path, '..', '..'))

    # set current directory
    os.chdir(directory)

    return directory


def get_config() -> ConfigParser:
    """Get config.cfg file

    Returns:
    --------
    ConfigParser: Config content
    """
    config_path = os.path.join(set_current_directory(), 'config.cfg')
    
    try:
        config = ConfigParser(default_section=DEFAULT_SECTION)
        config.read(config_path, 'utf-8')
        
        # Validate that all sections and their values are non-empty
        for key, value in config.items(DEFAULT_SECTION):
            if not value.strip():
                add_log.error(f"Empty or invalid value found in section '{DEFAULT_SECTION}', key '{key}'")
                raise ValueError(f"Empty or invalid value found in section '{DEFAULT_SECTION}', key '{key}'")
        
        return config[DEFAULT_SECTION]
    
    except Exception as e:
        add_log.error(f"Error loading configuration: {e}")
        raise ImportError(f"Error loading configuration: {e}")


# Create log folder
try: 
    os.mkdir(set_current_directory() + '/log/')
except:
    pass


# Logging config/call
logging.basicConfig(filename=set_current_directory() + '/log/LOG_' + datetime.now().strftime("%Y%m") + '.log', 
                    filemode='a', 
                    format=FORMAT,
                    level='INFO',
                    encoding='utf-8')


add_log = logging.getLogger(__name__)
