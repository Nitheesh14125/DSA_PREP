def minimum_element(arr):
    if len(arr) == 0:
        return None 
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min :
            min = arr[i]
    return min 

arr = [10,20,30,40]
print(minimum_element(arr))