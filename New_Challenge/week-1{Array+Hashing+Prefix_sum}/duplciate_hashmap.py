def duplicate_hashmap(arr):
    seen = set()

    for i in range(len(arr)):
        if arr[i] in seen:
            return True
        seen.add(arr[i])
    return False

l = [100,60,210,10,100]
print(duplicate_hashmap(l))