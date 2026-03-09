def missing_number(arr):
    if len(arr) <= 1:
        return None 
    n = len(arr)+1
    total_sum = n*(n+1)//2
    sum = 0 
    for i in range(len(arr)):
        sum = sum + arr[i]

    final = total_sum - sum
    return final 

l = [1,2,3,5]
print(missing_number(l))