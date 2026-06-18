def union_arr(a, b):
    seen = set()
    
    for num in a:
        seen.add(num)
        
    for num in b:
        seen.add(num)
        
    return sorted(list(seen))

# Defining the arrays
a = [1, 2, 3, 4, 5]
b = [1, 4, 7, 8, 6]

# Running the function and printing the result
result = union_arr(a, b)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8] 