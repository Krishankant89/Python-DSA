def removeDuplicates(arr):
    
    seen = set()
    
    for num in arr:
        seen.add(num)
        
    return list(seen)

arr = [1,2,3,2,1,2]
print(removeDuplicates(arr))