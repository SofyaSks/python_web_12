# Программа спрашивает год рождения. Необходимо учесть, что помимо
# года рождения может быть введён любой мусор. Дождаться корректного ввода, не используя функцию isdigit

from datetime import datetime
try:
    year = int(input('Введите год рождения: '))
    if year > datetime.now().year:
        raise ValueError
    if year < 1900:
        raise ValueError
except ValueError:
    print('Неверное значение')

# year = int(input('Введите год рождения: '))
# if year > datetime.now().year:
#     raise ValueError('Будущее ещё не наступило')
# if year < 1900:
#     raise ValueError('Столько не живут')

# С клавиатуры вводятся целые числа "x". Выводить обратные им (1/x) до возникновения ошибки деления на ноль. Вывести "расчёт окончен" и указать количество введенных чисел

try:
    count = 0
    num = 1
    while num != 0:
        num = int(input('Введите число: '))
        print(1 / num)
        count+=1
except ZeroDivisionError:
    print(f'Расчёт окончен. Количество введённых чисел: {count}')


# С клавиатуры вводятся вещественные числа. Выводить обратные им (1/x) до возникновения ошибки деления на ноль. Вывести "расчёт окончен" и указать количество введенных чисел

try:
    count = 0
    num = 1
    while num != 0:
        num = float(input('Введите число: '))
        print(1 / num)
        count+=1
except ZeroDivisionError:
    print(f'Расчёт окончен. Количество введённых чисел: {count}')

