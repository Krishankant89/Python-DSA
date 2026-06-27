def longest_subarray_sum_k(arr,k):
    n = len(arr)
    max_len = 0
    
    for i in range(n):
        current_sum = 0
        
        for j in range(i,n):
            current_sum += arr[j]
            
            if current_sum == k:
                length = j - 1 + 1
                max_len = max(max_len, length)
    return max_len

arr = [1,2,3,1,1,1,1]
k = 6
result = longest_subarray_sum_k(arr,k)
print(result)