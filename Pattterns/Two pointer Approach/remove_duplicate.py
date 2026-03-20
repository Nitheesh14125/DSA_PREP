#Pattern : same direction two pointer 
#Reason : We use two pointers where
# j scans the array (fast pointer)
# i tracks the position of unique elements (slow pointer) 
# When we find a new (different) element, we increment i and place it at position i


def remove_duplicate(arr):
    i = 0 
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            i =i +1 
            arr[i] = arr[j]
    return arr[:i+1] # for modified array and the "return arr[i+1] for the unique elements"
arr = [10,10,10,20,20,20,30]
print(remove_duplicate(arr))



# brute force 

def brute_force(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] != arr[i]:
                i = i + 1 
                arr[i] = arr[j]
    return i+1 

print(brute_force(arr))