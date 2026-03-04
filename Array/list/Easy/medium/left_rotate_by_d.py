def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start = start + 1
        end = end - 1 

def left_rotate(arr,d):
    n = len(arr)

    if n <= 1:
        return None
    
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    return arr

l =[10,20,30,40,50]
d = 3 
print(left_rotate(l,d))
