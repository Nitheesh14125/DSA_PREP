def two_sum(arr,target):
    left = 0 
    right = len(arr) -1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left+1,right+1]#logic correct man but the index result show to seen clearly
        elif s < target:
            left = left + 1
        else:
            right = right - 1 

l =[2,3,4]
target = 6
print(two_sum(l,target))