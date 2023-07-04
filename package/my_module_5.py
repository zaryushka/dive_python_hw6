"""
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8x8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

"""

import numpy as np
import random

board = np.zeros((8,8), dtype=int)

positions = random.sample(range(64), 8)
# print(positions)

for pos in positions:
    row = pos // 8
    col = pos % 8
    board[row, col] = 1

print(board)

def list_positions(board):
    list_board = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                list_board.append((i, j))
    return list_board


# print(list_board)
# print(type(list_board))


def chek_position(list_board):
    for i in range(len(list_board)):
        row_1, col_1 = list_board[i]
        for j in range(i + 1, len(list_board)):
            row_2, col_2 = list_board[j]
            if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_2 - col_2):
                return False
   
    return True


list_board = list_positions(board)
result = chek_position(list_board)
# print(result)


# здесь я попыталась написать блок для вывода 4 успешных расстановок
# succs_position = []
# while len(succs_position) < 1:
#     if result is True:
#         if result not in succs_position():
#             succs_position.append(list_board)

# for s_p in succs_position:
#     print(s_p)
#     print(chek_position(s_p))



def print_result():
    if result is True:
        print('ни один ферзь друг друга не бьет')
    else:
        print('есть хотя бы одна пара бьющих друг друга ферзей')



if __name__ == '__main__':
     
    print_result()

