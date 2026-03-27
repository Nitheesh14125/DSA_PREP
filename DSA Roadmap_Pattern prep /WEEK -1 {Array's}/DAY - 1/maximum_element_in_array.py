#pattern = traversal elements in array and compare them with if condition 
#Reason = i will be the best we have to check all elements so traversal need to done
#Brute force idea = lets sort the array and then lets return the len(arr) - 1 but it wont workout in all cases 
#pesudo code = 
''' max = 0 variable 
    iterate all elements in the array 
    if iterate > max 
    max = iterate 
    loop until end of the array 
    return max'''

#code 

def max_element(arr):
    if len(arr) == 0:
        return None 
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    
    return max 

arr = [10,20,30,40]
print(max_element(arr))

#time complexity = o(n)
