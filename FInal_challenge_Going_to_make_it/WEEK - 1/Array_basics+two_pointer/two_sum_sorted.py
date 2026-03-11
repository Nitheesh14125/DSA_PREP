def two_sum_sorted(arr,target):
    left = 0 
    right = len(arr) - 1
    while left < right :
        current_sum =  arr[left] + arr[right]
        if current_sum == target:
            return [left,right]
        elif current_sum < target:
            left = left + 1 
        else:
            right = right - 1

l = [2,7,9,11]
print(two_sum_sorted(l,9))