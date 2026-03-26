def first(arr,target):
    left = 0 
    right = len(arr)-1
    ans = - 1 

    while left <=right:
        mid = (left+right)//2 
        if arr[mid] == target:
            ans = mid 
            right = mid - 1 
        elif arr[mid] > target:
            right = mid -1 
        else:
            left = mid + 1
    return ans

def last(arr,target):
    left = 0 
    right = len(arr)-1
    ans = - 1 

    while left <=right:
        mid = (left+right)//2 
        if arr[mid] == target:
            ans = mid 
            left = mid + 1 
        elif arr[mid] > target:
            right = mid -1 
        else:
            left = mid + 1
    return ans


def position(arr,target):
    first_index = first(arr,target)
    last_index = last(arr,target)
    return [first_index,last_index]


arr = [1, 2, 4, 4, 4, 5, 6]
target = 4
print(position(arr, target))