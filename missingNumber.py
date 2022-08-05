class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(0, len(nums)+1))-sum(nums)
