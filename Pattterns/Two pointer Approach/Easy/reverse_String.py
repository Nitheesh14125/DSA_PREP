#pattern : opposite side two pointer approach 
#reason : we will use left = 0 and right = len - 1 and then we will swap there location as 
# arr[left],arr[right] = arr[rigth],arr[left]
#and then we will writeen the array 
#time complexity = o(n)

def reverse_string(arr):
    left = 0 
    right = len(arr)-1 
    while left < right :
        arr[left],arr[right] = arr[right],arr[left]
        left = left + 1
        right = right - 1
    return arr

arr= ['h','e','l','l','o']
print(reverse_string(arr))
