def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr1 = [1,5,9,6,3,4,6,0]
bubbleSort(arr1)
print(arr1)
