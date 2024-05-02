from logger import logger_config
from random import randint

log = logger_config(__name__)

class RangeIsNotCorrect(Exception):
    """Проверка правильности диапазона"""

try:
    start = int(input())
    end = int(input())
except ValueError:
    log.exception('Не удалось преобразовать значения, попробуйте другие коэффициенты')
    print('Не удалось преобразовать значения, попробуйте другие коэффициенты')

    
def check_range(start, end):
    if start < 0 or end < start:
        raise RangeIsNotCorrect
    return randint(start, end)

try:
    rand_number = check_range(start, end)
    log.info(f'Случайное число равно {rand_number}')
    print(rand_number)
except RangeIsNotCorrect:
    print('Диапазон не корректен. Начальное значение не должно быть меньше нуля и конечное значение не должно быть меньше начального')
    log.exception('Диапазон не корректен. Начальное значение не должно быть меньше нуля и конечное значение не должно быть меньше начального')
    
