def intersection(arr1,arr2):
    visited = [False] * len(arr2)
    result = []
    
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j] and not visited[j]:
                           result.append(arr1[i])
                           visited[j] = True
                           break
    return result

arr1 = [1,2,2,3,4]
arr2 = [2,2,3,3]
print(intersection(arr1,arr2))