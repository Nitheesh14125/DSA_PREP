def count_occurance(arr,target):
    if len(arr) == 0 :
        return None 
    
    count = 0 
    for i in range(len(arr)):
        if arr[i] == target:
            count = count + 1 
    return count 

arr = [1,2,2,2,2,2,2,2,3]
print(count_occurance(arr,2))