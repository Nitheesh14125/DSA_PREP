def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start = start + 1
        end = end - 1

def left_rotate(arr,d):
    n = len(arr)

    if len(arr) <= 1 :
        return arr
    
    d = d % n 
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

    return arr

l = [10,20,30,40,50]
print(left_rotate(l,2))