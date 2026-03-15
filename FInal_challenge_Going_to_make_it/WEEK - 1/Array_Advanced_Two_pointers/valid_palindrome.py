def valid_palindrome(str):
    left = 0 
    right = len(str)- 1
    while left < right :
        if str[left] != str[right]:
            return False
        left = left + 1 
        right = right - 1
    return True 

str= "MADAM"
print(valid_palindrome(str))


#Time complexity = o(n)
#space complexity = o(1)  might be change if the left and right variable 