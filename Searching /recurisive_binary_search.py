def recbinary(arr,target,left,right):
    if left > right :
        return -1
    mid = (left+right)//2
    if arr[mid] == target:
        return mid 
    elif arr[mid] > target:
        return recbinary(arr,target,left,mid-1)
    else:
        return recbinary(arr,target,mid+1,right)

def binary(arr,target):
    return recbinary(arr,target,0,len(arr)-1)


arr = [10,20,30,40,50,60]
target = 40 
print(binary(arr,target))
