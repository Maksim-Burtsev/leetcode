from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        ans_num = 0
        for i in set(nums):
            elem_count = nums.count(i)
            if elem_count > max_count:
                max_count = elem_count
                ans_num = i
        return ans_num
