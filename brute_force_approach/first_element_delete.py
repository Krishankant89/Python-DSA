arr = [10,20,30,40,50]
size = len(arr)
print("Before Deletion", arr)
for i in range(1, size):
    arr[i -1] = arr[i]
    
new_arr = [0] * (size -1)
for i in range(size -1):
    new_arr[i] = arr[i]
    
arr = new_arr

print("Array Brute Force Deletion", arr)