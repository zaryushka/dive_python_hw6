"""модуль для угадывания пользователем рандомного числа
Создайте модуль с функцией внутри. 
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
Функция выводит подсказки “больше” и “меньше”. 
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""


from random import randint


__all__ = ['rand_num']

def rand_num(lower_limit, upper_limit, attemts):
    number_game = randint(lower_limit, upper_limit)
    for i in range(attemts):
        number = int(input('введите число: '))
        if number < number_game:
            print('Загаданное число больше')
        elif number > number_game:
            print('Загаданное число меньше')
        else:
            print('Правильно')
            return True
    print('попытки закончились')
    return False



if __name__ == '__main__':

    result = rand_num(0, 100, 5)
    print(f'результат {result}')
