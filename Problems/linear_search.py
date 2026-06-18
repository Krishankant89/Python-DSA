def linear_search(arr,target):
    n = len(arr)
    
    for i in range(n):
        if arr[i] == target:
            return i
        
    return -1

arr = [1,5,1,6,8,3]
target = 1
result = linear_search(arr,target)
print(result)