def bubbleSort(arr):
    #取出数组长度
    n=len(arr)

    #第一层循环,依次取出最大值
    for i in range(0, n):
        #第二层循环,依次比较
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("排序后的数组:")
print(arr)