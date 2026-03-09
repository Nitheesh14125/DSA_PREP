def duplicate_array_single_loop_sorted(arr):
    i = 0 
    while i < len(arr):
        if arr[i] == arr[i-1]:
            return True 
        i = i+ 1
    return False

l = [10,15,5,20,20,21]
print(duplicate_array_single_loop_sorted(l))
