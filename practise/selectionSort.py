def selectionSort2(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr

arr1 = [9,0,4,5,1,3,9,2,5]
print(selectionSort2(arr1))

