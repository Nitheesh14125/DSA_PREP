def leaders(arr):
    leader = []
    for i in range(0,len(arr)):
        for j in range(1,len(arr)):
            if arr[i] > arr[j]:
                leader.append(arr[i])
                break
    return leader 
l = [16,17,4,3,5,2]
print(leaders(l))