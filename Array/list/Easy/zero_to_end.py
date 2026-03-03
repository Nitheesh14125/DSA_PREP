def zeros_to_end(arr):
    if len(arr) <= 0:
        return None
    j = 0
    for i in range(1,len(arr)):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j = j + 1 
    return arr

l = [10,0,121,0,0,12,0]
print(zeros_to_end(l))