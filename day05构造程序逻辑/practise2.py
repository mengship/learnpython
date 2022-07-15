"""
正整数的反转
Version: 0.1
Author: 王昱棋

"""

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

num = 157
reversed_num = 7
num = 15

reversed_num = 75
num = 1