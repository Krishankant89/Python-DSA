size = int(input("Enter the size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i}: "))
    arr.append(value)

insert_value = int(input("Enter the value to insert at last: "))

arr.append(insert_value)

print("Array after insertion:", arr)