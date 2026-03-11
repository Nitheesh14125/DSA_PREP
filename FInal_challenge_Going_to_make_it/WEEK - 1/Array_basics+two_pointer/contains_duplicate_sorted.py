def contains_duplicate(arr):
    for i in range(len(arr)):
        if arr[i] == arr[i-1]:
            return True
    return False

l = [2,100,1,55,1]
print(contains_duplicate(l))