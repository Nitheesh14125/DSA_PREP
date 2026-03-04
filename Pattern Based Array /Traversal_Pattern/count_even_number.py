def count_even(arr):
    if len(arr) <= 1:
        return None 
    count = 0 
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            count = count + 1
    return count 

l = [1,3,5,7,9]
print(count_even(l))