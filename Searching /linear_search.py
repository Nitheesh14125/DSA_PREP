def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return - 1

l = [10,311,12,1,222]
print(linear_search(l,12))