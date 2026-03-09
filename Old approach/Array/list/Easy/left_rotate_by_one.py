def left_rotate(arr):
    if len(arr) <= 1:
        return arr or None
    first = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]

    arr[-1] = first
    return arr

l = [1,0,0,0,0]
print(left_rotate(l))

