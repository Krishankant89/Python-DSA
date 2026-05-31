size = int(input("Enter the size of array:"))

arr = []

for i in range(size):
    value = int(input(f"Enter the elements {i}:"))
    arr.append(value)
    
index = int(input("enter the index to delete:"))

if 0 <= index < len(arr):
    arr.pop(index)
    print("Array after deletion", arr)
else:
    print("Invalid index")