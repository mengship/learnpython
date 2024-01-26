def bubbleSort(arr):
    # 取出数组长度
    n = len(arr)
    # 遍历所有数组元素
    # i 从0开始到 len-1
    for i in range(n):
        # Last i elements are already in place 最右侧的数据取不到,左闭右开
        for j in range(0, n - i - 1):
            print(j)
            # print(j+1)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("排序后的数组:")
print(arr)