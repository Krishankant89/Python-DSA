arr = [10,20,30,40,50,60]

last_index = -1

for i in range(len(arr)):
    if arr[i] is not None:
        last_index = i
    else:
        break
    
if last_index != -1:
    arr[last_index] = None
print(arr)