def second_largest(arr):
    fmax = arr[0]
    smax = arr[0]
    for i in range(len(arr)):
        if arr[i] > fmax:
            smax = fmax 
            fmax = arr[i]
        elif arr[i] < fmax and arr[i] > smax:
            smax = arr[i]

    return smax

arr = [10,20,30,40,50]
print(second_largest(arr))
  