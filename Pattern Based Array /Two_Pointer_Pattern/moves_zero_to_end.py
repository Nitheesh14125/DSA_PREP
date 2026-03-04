def moveZeroes(arr):
    j = 0

    for i in range(len(arr)):
         if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

l = [10,0,20,0]
print(moveZeroes(l))