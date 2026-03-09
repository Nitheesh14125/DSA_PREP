def two_sum_hashmap(arr,target):
    hashmap = {}
    for i in range(len(arr)):
        needed = target - arr[i]
        if needed in hashmap:
            return [hashmap[needed],i]
        hashmap[arr[i]] = i 

l = [10,20,30,40]
print(two_sum_hashmap(l,30))