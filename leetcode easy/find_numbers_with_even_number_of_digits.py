class Solution(object):
    def findNumbers(self, nums):
        return sum(len(str(num)) % 2 == 0 for num in nums)

nums = [12, 354, 2, 6789]
sol = Solution()
print(sol.findNumbers(nums))