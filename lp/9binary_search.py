def binary_search(list, num):
    head = 0
    tail = len(list) - 1
    mid = 0
    while head <= tail:
        mid = (head + tail) // 2
        if list[mid] == num:
            return mid
        elif list[mid] < num:
            head = mid + 1
        else:
            tail = mid + 1
    return -1


if __name__ == '__main__':
    temp = input('input sort num:')
    temp = temp.split(',')
    my_list = [int(x) for x in temp]
    num = eval(input('input search num:'))
    print(binary_search(my_list, num))
