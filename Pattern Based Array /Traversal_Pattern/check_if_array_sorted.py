def check_sorted(arr):
    if len(arr) <=1 :
        return None 
    i = 1
    while i < len(arr):
        if arr[i] < arr[i-1]:
            return False
        i = i + 1 
    return True
l = [10,20,3,40]
print(check_sorted(l))