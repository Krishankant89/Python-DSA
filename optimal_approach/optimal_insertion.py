def element_insertion():
    arr = []
    size = int(input("Enter the size of array:"))    
    for i in range(size):
        value = int(input(f"Enter the elements {i}:"))
        arr.append(value)
        
    
    position = int(input("Enter the position to insert"))
    insert_value = int(input("Enter the value to insert"))
    
    arr.insert(position, insert_value)
        
    print(arr)
element_insertion()