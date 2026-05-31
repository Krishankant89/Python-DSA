size = int(input("Enter the size of array:"))

arr = []

for i in range(size):
    value = int(input(f"Enter the elements {i}:"))
    arr.append(value)

element = int(input("Enter the value to insert:"))    


arr = arr + [0]

arr[size] = element
size += 1

print(arr)