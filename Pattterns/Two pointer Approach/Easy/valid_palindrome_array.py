#pattern : opposite Two pointer approach 
#reason : Becuase the palindrome me if we reverse a string or array we need to get the exact if 
#palindrome == reverse then true or else false 
# so that lets take left = 0 and right = len(arr)-1 so that we we check arr[left] != arr[right]
# return False and then increment left and decrement right to check and all 
#statifies are the loop return True 
#time complexity == o(n) if best case o(1)
def valid_palindrome(arr):
    left = 0 
    right = len(arr)-1 
    
    while left < right:
        if arr[left]!=arr[right]:
            return False 
        left = left + 1 
        right = right - 1
    return True 

arr1 =[1,2,3,4]
arr2 = [1,2,1]
print(valid_palindrome(arr1))
print(valid_palindrome(arr2))


#for the any type of string 
