def valid_palindrome_interview(s):
     
    result = ""
    s = s.lower()

    for i in range(len(s)):
        if s[i].isalnum():
            result = result + s[i]

    left = 0
    right = len(result)-1
    while left < right:
        if result[left] != result[right]:
            return False 
        left = left + 1
        right = right - 1 
    return True 

print(valid_palindrome_interview("A man, a plan, a canal: Panama"))
    