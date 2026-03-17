def sliding_window_fixed(arr,k):

    start = 0 
    end = 0 

    while end < len(arr):
        
        if (end-start+1) < k :
            end = end + 1 #creating a window clearly 

        elif (end - start + 1) == k : #window created 
            print(arr[start:end+1])

            start = start + 1 
            end = end + 1 # To slide the window until the end 


arr =[1,2,3,4,5,6]
sliding_window_fixed(arr,3)