def isSorted(arr):
    n = len(arr)
    
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            return False
        
    return True

arr = [2,1,3,4,5]
print(isSorted(arr))