def zero_to_end(arr):
    if len(arr) == 0:
        return None 
    j = 0 
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i] ,arr[j] = arr[j],arr[i]
            j = j + 1
    return arr

l = [0,10,20,30,0,40,0,0,0,0]
print(zero_to_end(l))
    
