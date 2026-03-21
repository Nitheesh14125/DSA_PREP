#pattern : same direction  two pointer approach 
#reason : we have to move all elements to zero we rather focusing on the zero we make i = 0 and 
# j = 1 fast  pointer and i will be the slow pointer as condition arr[i] != arr[j] we will swap 
# arr[i],arr[j] = arr[j],arr[i] then we will incrment the value or else we will try while implementing 
#time complexity = o(n)

def move_zeroes(arr):
    i = 0 
    for j in range(1,len(arr)):
        if arr[j] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            i = i +1 
    return arr

arr = [0,1,0,3,12]
arr1 = [0,0,1]
print(move_zeroes(arr))
print(move_zeroes(arr1))