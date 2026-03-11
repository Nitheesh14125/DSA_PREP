def move_zeroes(arr):
    i = 0 
    j = 0 
    while i < len(arr):
        if arr[i] != 0: 
            arr[i],arr[j] = arr[j],arr[i]
            j = j + 1
        i = i + 1 
    return arr 

l = [0,0,10,0,0,10]
print(move_zeroes(l))