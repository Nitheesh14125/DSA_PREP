def rotate_by_one(arr):
    if len(arr) <=1 :
        return None
    n = len(arr)
    last = arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    
    arr[0] = last 
    return arr

l = [10,20,30,40]
print(rotate_by_one(l))