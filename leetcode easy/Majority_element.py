class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        candidate = None
        count = 0
        
        for num in A:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate
