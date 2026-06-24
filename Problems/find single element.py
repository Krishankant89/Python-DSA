def single_number(arr):
    n = len(arr)
    xor = 0
    
    for i in range(n):
        xor = xor ^ arr[i]
        
    return xor
    
arr = [1,1,2,3,3,4,4]
result = (single_number(arr))
print(result)