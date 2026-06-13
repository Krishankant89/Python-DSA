def binary_search(arr,target):
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
             low = mid + 1
        
        else:
            high = mid - 1
            
    return -1

arr = [10, 35, 45, 65]
target = int(input("Enter the target value: "))

# Call the function and store the result
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")