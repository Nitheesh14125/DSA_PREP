#pattern : opposite sid two pointer 
#reason: when we use the normal approach of brute force then the time complexity will be o(n^3) for that 
# so firstly lets clear under the problem [a+b+c] = 0 the values should unique and no duplicates 
# first lets sort the array 
#lets take a i loop which iterate the complete array for i in range(Len(Arr))
#o remove the duplicate for if i > 0 and arr[i] == arr[i-1] just skip the current iteration loop and continue 
#take left = i + 1 and right = n - 1 (two pointer oppoiste side approach)
#while left < right :
# s= arr[i]+arr[left]+arr[right] 
#if s == 0 then append the values into variable res[] and similarly left = left + 1 and right = right - 1 
#elif s < 0 - left = left + 1
#else  right = right - 1

def three_sum(arr):
    arr.sort()
    res = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue 

        left = i + 1
        right = len(arr) - 1

        while left < right :
            s = arr[i]+arr[left]+arr[right] 

            if s == 0 :
                res.append([arr[i],arr[left],arr[right]])
                left = left + 1
                right = right - 1
            elif s < 0:
                left = left + 1
            else :
                right = right - 1
    return res 

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))