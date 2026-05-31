def create_array():
    
    arr = []
    
    for i in range(size):
        value = int(input(f"Enter the elements {i}:"))
        arr.append(value)
        
    for a in arr:
        print(a)
        
size = int(input("Enter the size of array:"))

create_array()