class Solution:
    def sum_of_matrix(self,arr):
    
        n = len(arr)
    
        for i in range(1, n):
            arr[i] += arr[i -1]
        
        return arr

arr = [1,2,3,4]
solver=Solution()
print(solver.sum_of_matrix(arr))