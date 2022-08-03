from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1

        while left != right:
            if nums[left] % 2 == 1:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1


        return nums

# 1 2 4 6 7 9 
# 9 2 4 6 7 1 
# 7 2 4 6 9 1
# 6 2 4 7 9 1 