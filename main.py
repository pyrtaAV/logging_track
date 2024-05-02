def main():
    some_str = 'abc'
    try:
        some_str = int(some_str)
    except ValueError:
        print('Переменная some_str не может быть преобразована')
    else:
        print(some_str)
    finally:
        print('Измените значение переменной some_str!')


