def duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return True 
    return False

l = [10,20,30,40]
print(duplicate(l))