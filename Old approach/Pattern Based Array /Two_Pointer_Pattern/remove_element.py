def remove_element(arr,value):
    i = 0 
    for j in range(len(arr)):
        if arr[i] != value:
            arr[i] = arr[j]
            i = i + 1
    return i


l =[10,20,30]
print(remove_element(l,10))
