def sorted_or_not(arr):
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

arr = [10,20,30,40,2]
print(sorted_or_not(arr)) 