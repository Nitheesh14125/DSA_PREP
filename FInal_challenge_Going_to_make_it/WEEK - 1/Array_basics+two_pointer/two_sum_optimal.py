def two_sum(arr,target):
    hashmap = {}

    for i in range(len(arr)):
        needed = target - arr[i]

        if needed in hashmap:
            return [hashmap[needed],i]
        
        hashmap[arr[i]] = i 
        