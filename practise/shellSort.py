def shellSort(arr):
    import math
    gap=1
    while(gap<len(arr)/3):
        gap = gap*3+1
    while gap>0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j]>temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap]=temp
        gap = math.floor(gap/3)
    return arr

arr1=[1,2,3,4,7,6,5,3,9,8,7,6,5,4]
print(shellSort(arr1))

