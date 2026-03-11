def square_sorted(arr):
    left = 0
    right = len(arr) - 1 

    result = [0]*len(arr)
    pos = len(arr) - 1

    while left <= right:
        sqr_left = arr[left] ** 2
        sqr_right = arr[right] ** 2 

        if sqr_left > sqr_right:
            result[pos] = sqr_left
            left = left + 1
        else:
            result[pos] = sqr_right
            right = right - 1
        
        pos = pos - 1 

    return result 

l = [2,4,1]
print(square_sorted(l))