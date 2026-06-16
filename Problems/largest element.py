def largest_element(arr):
    if not arr:
        return None
    
    n = len(arr)
    largest = arr[0]
    
    for i in range(1,n):
        if arr[i] > largest:
            largest = arr[i]
            
    return largest

arr = [456,1231,52352,123124]
sol = largest_element(arr)
print(sol)