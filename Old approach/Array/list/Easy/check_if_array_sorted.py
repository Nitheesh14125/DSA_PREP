def array_sorted(arr):
    if len(arr) == 0:
        return None 
    i = 0 
    while i < len(arr):
        if arr[i] < arr[i-1]:
            return False
        i = i+ 1
    return True 

l = [10,20,30,40,50]
l1 = [10,20,3,211,1]

print(array_sorted(l))
print(array_sorted(l1))
