def largest_arr_element(arr):
    if len(arr) <= 1: 
        return None
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

l =[10,20,30,40,50]
print(largest_arr_element(l))