from package.my_module_2 import rand_num


result = rand_num(0, 100, 5)
print(f'результат {result}')



# Для запуска функции в командной строке
# from sys import argv

# args = [int(arg) for arg in argv[1:]] # преобразуем в целые числа и сохраняем в список args

# if rand_num(*args):
#   print('Вы угадали')
# else:
#   print('Вы не угадали')

# python .\main2.py 1 100 5 - запуск в командной строке