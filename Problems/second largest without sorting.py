def second_largest_number(arr):
    
    n = len(arr)
    
    if n < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
            
        elif num < largest and num > second_largest:
            second_largest = num
            
    if second_largest == float('-inf'):
        return None
    
    return second_largest

arr = [12,35,45,67,2]
print(arr)
print(second_largest_number(arr))