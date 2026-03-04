def minimum(arr):
    if len(arr) <= 1:
        return None
    
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min 

l = [10,20,3,0,212]
print(minimum(l))