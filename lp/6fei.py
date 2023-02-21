def fei(num):
    if num <= 0:
        print('illegal')
        return

    if num == 1 or num == 2:
        return 1
    else:
        return fei(num - 1) + fei(num - 2)


if __name__ == '__main__':
    while True:
        num = eval(input('please input a num:'))
        print(fei(num))
