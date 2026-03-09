def duplicate_arr(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return True 
    return False

l = [100,60,210,10,100]
print(duplicate_arr(l))

#time complexity = o(n^2)