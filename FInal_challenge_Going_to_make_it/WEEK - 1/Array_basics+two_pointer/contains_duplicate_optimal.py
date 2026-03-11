def contains_duplicate(arr):
    seen = set()

    for i in range(len(arr)):
        if arr[i] in seen:
            return True
        seen.add(arr[i])
    return False 

l = [10,20,30,40]
print(contains_duplicate(l))