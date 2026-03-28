def largest(arr):
    maxe = arr[0]
    for i in range(len(arr)):
        if arr[i] > maxe:
            maxe = arr[i]
    return maxe 

l = [10,20,30,40,50]
print(largest(l))