def duplicates(arr):
    if len(arr) == 0:
        return None 
    i = 0
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            i = i +1 
            arr[i] = arr[j]    
    return arr[:i+1]
l = [10,20,30,40]
l1 = [10,10,20,20,30,30]
print(duplicates(l))
print(duplicates(l1))
