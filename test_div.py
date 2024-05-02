from logger import logger_config

log = logger_config(__name__)

log.info(f"Testing the custom logger for module {__name__}...")

def test_division(x,y):
    try:
        x/y
        log.info(f"x/y successful with result: {x/y}.")
    except ZeroDivisionError as err:
        log.exception("ZeroDivisionError")