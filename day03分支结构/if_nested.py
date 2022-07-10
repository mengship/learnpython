"""
分段函数求值
        3x - 5 (x > 1)
f(x) =  x + 2 (-1 <= x <= 1)
        5x + 3 (x < -1)

Version: 0.1
Author: 王昱棋
Flat is better than nested
提倡代码"扁平化"因为嵌套结构的嵌套层次多了之后会严重的影响代码的可读性，
所以能使用扁平化的结构就不要使用嵌套
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
