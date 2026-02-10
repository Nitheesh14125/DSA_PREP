def remove_duplicate_array(arr):
    i = 0 
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            i = i +1 
            arr[i] = arr[j]
    return i + 1

arr = [1,1,1,2,3,3,3,4,4,4,4]
print(remove_duplicate_array(arr))