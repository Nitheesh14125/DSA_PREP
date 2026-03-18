def maximum_average(arr,k):

    start = 0 
    end = 0 
    max_sum = float('-inf') 
    window_sum = 0 

    while end < len(arr):
        window_sum = window_sum + arr[end]
        if (end - start +1) < k:
            end = end + 1

        elif (end-start + 1) == k:

            max_sum = max(max_sum,window_sum)

            window_sum = window_sum - arr[start]
            start = start + 1
            end = end + 1

    return max_sum /k
    


arr = [1,2,3,4,5]
k = 3 
print(maximum_average(arr,k))