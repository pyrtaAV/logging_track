from logger import logger_config
from test_div import test_division

log = logger_config(__name__)

log.info(f"Testing the custom logger for module {__name__}...")

x_vals = [2,3,6,4,10]
y_vals = [5,7,12,0,1]

for x_val,y_val in zip(x_vals,y_vals):
    x,y = x_val, y_val
    # вызов test_division
    test_division(x,y)
    log.info(f"Call test_division with args {x} and {y}")