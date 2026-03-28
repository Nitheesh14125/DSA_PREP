def second_largest(arr):
    first = -1
    second = -1 

    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]

    return second

l = [10,20,30,40,50,50,40]
print(second_largest(l))

