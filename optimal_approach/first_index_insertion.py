def first_index_optimal():
    arr = []
    
    size = int(input("Enter the size of array:"))
    
    for i in range(size):
        value = int(input(f"Enter the elements {i}:"))
        arr.append(value)
        
    new_value = int(input("Enter the value to insert at first:"))
    
    arr.insert(0, new_value)
    
    print("Updated array",arr)
    
first_index_optimal()