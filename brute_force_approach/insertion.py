def element_insertion():
    arr = []
    size = int(input("Enter the size of array:"))    
    for i in range(size):
        value = int(input(f"Enter the elements {i}:"))
        arr.append(value)
        
    
    position = int(input("Enter the position to insert"))
    insert_value = int(input("Enter the value to insert"))
    
    arr = arr + [0]
    
    for i in range(size, position, -1):
        arr[i] = arr[i -1]
        
        arr[position] = insert_value
        
        print("Updated array",arr)
        
element_insertion()