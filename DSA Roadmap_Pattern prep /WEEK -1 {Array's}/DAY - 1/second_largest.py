def second_largest(arr):
    f_max = arr[0]
    s_max = arr[0]

    for i in range(len(arr)):
        if arr[i] > f_max:
            s_max = f_max
            f_max = arr[i]
        elif f_max < arr[i] < s_max:
            s_max = arr[i]
    return s_max 

arr = [10,20,30,40,50]
print(second_largest(arr))