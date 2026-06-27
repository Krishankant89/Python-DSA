def longest_subarray(arr,k):
    prefix_map = {}
    prefix_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        if prefix_sum == k:
            max_len = i + 1
            
        rem = prefix_sum - k
        
        if rem in prefix_map:
            length = i - prefix_map[rem]
            
            max_len = max(max_len,length)
            
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
            
    return max_len

arr = [1,2,3,1,1,1,1]
k = 6
result = longest_subarray(arr,k)
print(result)