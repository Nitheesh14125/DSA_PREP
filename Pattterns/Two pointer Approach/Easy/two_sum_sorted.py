#Pattern: opposite two pointer approach 
#reason: we will use this because the array is been sorted and then the lets point 
#left = 0 and right = len(Arr)-1 and the by the this in while we take sum_of = arr[left]+arr[right]
#if sum_of == target return the address or else sum_of > target then right = right -1 
#else left = left +1 
# works only for sorted which stored will check the order left lower and increasing and right higher 

def two_sum_sorted(arr,target):
    left = 0 
    right = len(arr)-1
    while left < right:
        sum_of = arr[left] + arr[right]
        
        if sum_of == target:
            return [left+1,right+1]
        elif sum_of > target:
            right = right - 1 
        else:
            left = left + 1

arr = [2,4,9,10]
print(two_sum_sorted(arr,6))