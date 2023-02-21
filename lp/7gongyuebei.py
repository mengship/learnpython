#
def gongyue(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1


def gongbei(num1, num2):
    return num1 * num2 // gongyue(num1, num2)


if __name__ == '__main__':
    while True:
        num1, num2 = eval(input('please input two num:'))
        if num1 > 0 and num2 > 0:
            print(gongyue(num1, num2))
            print(gongbei(num1, num2))
        else:
            print('illegal')
