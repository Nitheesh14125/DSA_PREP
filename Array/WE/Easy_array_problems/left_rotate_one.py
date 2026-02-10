def left_rotate_one(arr):
    first = arr[0]
    n = len(arr)
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[n-1] = first 
    return arr

arr = [1,2,2,4,5]
print(left_rotate_one(arr))