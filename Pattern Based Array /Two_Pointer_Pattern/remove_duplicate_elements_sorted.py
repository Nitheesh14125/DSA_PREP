def remove_duplicate(arr):
    i = 0 
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i= i + 1
            arr[i] = arr[j]
    return i+1 , arr[:i+1] #it returns both unique elements and the unique array 

l = [10,10,20,30]
print(remove_duplicate(l))