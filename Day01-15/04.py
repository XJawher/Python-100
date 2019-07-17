# -*- coding: utf-8 -*
"""python 的循环结构大致分为两种,一种是 for in 一种是 while 循环"""

# sum = 0
# for x in range(20):
#     sum += x
# print(sum)

# import random

# def random():
#     counter = 0
#     answer = 20
#     while True:
#         counter += 1
#         number = int(input('请输入: '))
#         if number < answer:
#             print('大一点')
#         elif number > answer:
#             print('小一点')
#         else:
#             print('恭喜你猜对了!')
#             break
#     print('你总共猜了%d次' % counter)
#     if counter > 7:
#         print('你的智商余额明显不足')

# random()

# row = int(input('请输入行数: '))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')
#     print()

# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()


def multiplication():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(('%d*%d=%d' % (i, j, i * j)), end='\t')
        print()


multiplication()