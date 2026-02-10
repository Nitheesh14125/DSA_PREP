def largest_number(arr):
    fmax = arr[0]
    for i in range(len(arr)):
        if arr[i] > fmax:
            fmax = arr[i]
    return fmax

arr = [10,20,30,4,133,999]
print(largest_number(arr))