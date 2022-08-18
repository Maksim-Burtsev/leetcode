import heapq

class Solution:
    @staticmethod
    def findKthLargest(nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
