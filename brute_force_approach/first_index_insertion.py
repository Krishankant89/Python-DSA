def first_index():
    
    arr = []
    
    size = int(input("Enter the size of array:"))
    
    for i in range(size):
        value = int(input(f"Enter the elements {i}:"))
        arr.append(value)
    
    new_value = int(input("Enter the value to insert:"))
    
    arr.append(0)
    
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
        
    arr[0] = new_value
    
    print(arr)
    
first_index()