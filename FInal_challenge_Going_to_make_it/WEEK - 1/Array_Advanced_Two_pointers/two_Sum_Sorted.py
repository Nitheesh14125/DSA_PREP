def two_sum_sorted(arr,target):
    left = 0
    right = len(arr)-1

    while left < right :
        sum = arr[left] + arr[right]
        if sum == target:
            return [left,right]
        elif sum < target:
            left = left + 1
        else:
            right = right - 1 
    return None 

l=[2,4,6,8,10]
print(two_sum_sorted(l,8))
