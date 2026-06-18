def linear_search_duplicates(arr,target):
    
    n = len(arr)
    indices = []
    
    for i in range(n):
        if arr[i] == target:
            indices.append(i)
            
    return indices if indices else -1

arr = [1,4,3,4,2]

target = 4

result = linear_search_duplicates(arr,target)

print(result)