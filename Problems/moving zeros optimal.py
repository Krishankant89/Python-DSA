def move_zeros(arr):
    
    j = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            
            j += 1
            
    while j < len(arr):
        arr[j] = 0
        j += 1
    return arr

arr = [1,0,2,3,0,4]
print(move_zeros(arr))