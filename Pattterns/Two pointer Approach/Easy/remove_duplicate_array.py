#pattern : same direction two pointer approach 
#reason : by this pattern we have two pointer i and j, j is a fast pointer which iterates fast 
#complete array but the i is an slow pointer which increment only the condition is true 
# and by which we will increment i and assign arr[i] = arr[j] and return unique we will go with 
# return i + 1

def remove_duplicate(arr):
    i = 0 
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            i = i + 1 
            arr[i] = arr[j]
    return i + 1 # if you want to return the array then arr[:i+1]
arr1 = [1,1,2]
arr2=[0,0,1,1,1,2,2,3,3,4]
print(remove_duplicate(arr1))
print(remove_duplicate(arr2))