import functools
import logging
import requests
from pathlib import Path


# logger function
def create_logger(name: str = None, log_path: Path = Path('log.log')):
    """
    Creates a logging object and returns it
    """
    logger_name = name if name else __name__
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler(log_path)
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    # add handler to logger object
    logger.addHandler(fh)

    return logger


# logging decorator function
def logging_decor(function):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logger = create_logger()
        try:
            return function(*args, **kwargs)
        except Exception:
            logger.exception("Logging decorator handle error")
            raise

    return wrapper


# fetch json function for api_requests
@logging_decor
def fetch_json(url, params=None):
    """
    returns JSON from url
    """
    # url берем из конфига

    result = requests.get(url, params=params)
    result.raise_for_status()

    return result.json()