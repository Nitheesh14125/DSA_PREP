def second_largest(arr):
    if len(arr) <= 1:
        return None 
    
    largest = arr[0]
    s_largest = None 

    for i in range(len(arr)):
        if arr[i] > largest:
            s_largest = largest 
            largest = arr[i]
        elif largest > arr[i] > s_largest:
            s_largest = arr[i]
    return s_largest

l = [10,20,30,40,50]
l1 = [10,10,10,10,10]
l2 = [10,20,30,30,40,40]

print(second_largest(l))
print(second_largest(l1))
print(second_largest(l2))
