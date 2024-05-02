from logger import logger_config
import math

log_quest_5 = logger_config(__name__)

class DiscriminantLowerNull(Exception):
    """Возникает когда дискриминант меньше нуля"""
    
def discriminant(a, b, c):
    """Функция для расчета дискриминанта и проверка дискриманта на отрицательное число"""
    discr = b ** 2 - 4 * a * c
    log_quest_5.info("Дискриминант D = %.2f" % discr)
    if discr < 0:
        raise DiscriminantLowerNull
    return discr

def disc_more_or_equals(discr):
    """Функция для расчета корней в случае если дискриминант больше или равен нулю"""
    if discr == 0:
        x = -b / (2 * a)
        log_quest_5.info(f"Так как дискриминант равен нулю корень всего один и он равен {x:.2f}")
        print(f"Так как дискриминант равен нулю корень всего один и он равен {x:.2f}")
    else:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        log_quest_5.info(f"Первый корень равен: {x1:.2f}, Второй корень равен {x2:.2f}")
        print(f"Первый корень равен: {x1:.2f}, Второй корень равен {x2:.2f}")

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
except ValueError:
    log_quest_5.error('Не удалось преобразовать значения, попробуйте другие коэффициенты')
    print('Не удалось преобразовать значения, попробуйте другие коэффициенты')

try:
    discr = discriminant(a, b, c)
except DiscriminantLowerNull:
    log_quest_5.exception('Дискриминант меньше нуля попробуйте другие коэффициенты')
    print('Дискриминант меньше нуля попробуйте другие коэффициенты')
else:
    disc_more_or_equals(discr)
