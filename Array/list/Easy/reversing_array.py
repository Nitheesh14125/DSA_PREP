def reversing_array(arr):
    if len(arr) == 0:
        return None 
    left = 0 
    right = len(arr) - 1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left = left + 1
        right = right -1 
    return arr

l = [10,20,30,40,50]
print(reversing_array(l))