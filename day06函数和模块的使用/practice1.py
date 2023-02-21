"""
输入M和计算C(M,N)
Version: 0.1
Author: 王昱棋
"""

m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fm_n = 1
for num in range(1, m - n + 1):
    fm_n *= num
print(fm)
print(fn)
print(fm_n)
print(fm // fn // fm_n)