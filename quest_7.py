from logger import logger_config

log = logger_config(__name__)

numbers = [4, 8, 6, 5, 3, 2]
try:
    average = sum(numbers) / len(numbers)
    log.info(f'Среднее арифметическое списка равно {average:.2f}')
    print(f'Среднее арифметическое списка равно {average:.2f}')
except TypeError:
    log.exception('Передан неправильный тип данных')
    print('Передан неправильный тип данных')
