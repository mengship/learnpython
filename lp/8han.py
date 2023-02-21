def move(n, a, b, c):
    # a 借助b，放到c
    if n == 1:
        print(a, '->', c)
    else:
        move(n - 1, a, c, b)
        # 将 n-1 从 a 借助 c 放到 b
        print(a, '->', c)
        # 将 a 上最大的放到 c
        move(n - 1, b, a, c)
        # 将 n-1 从 b 放到 c


if __name__ == '__main__':
    while True:
        num = eval(input('please input num:'))
        move(num, 'A', 'B', 'C')
