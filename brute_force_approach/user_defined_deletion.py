size = int(input("Enter the size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i}: "))
    arr.append(value)

index = int(input("Enter the index to delete: "))

if index < 0 or index >= size:
    print("Invalid Index")
    
else:
    for i in range(index, size -1):
        arr[i] = arr[i + 1]
        
    arr.pop()
    
    size -= 1
    
    print("Array after deletion", arr)