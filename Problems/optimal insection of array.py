def intersection(arr1,arr2):
    i = 0
    j = 0
    result =[]
    
    while i < len(arr1) and j < len(arr2):
        
        if arr1[i] < arr2[j]:
            i += 1
        if arr2[j] < arr1[i]:
            j += 1
            
        else:
            result.append(arr1[i])
            i += 1
            j += 1
            
    return result

arr1 = [1,2,3,4,4]
arr2 = [2,3,4]
print(intersection(arr1,arr2))