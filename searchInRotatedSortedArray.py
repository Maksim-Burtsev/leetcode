# [1,2,3,4,5]

# [3,4,5,1,2]
# [2,3,4,5,1]
# [4,5,1,2,3]

# [1,2,3,4,5,6]

# [4,5,6,1,2,3]
class Solution:
    def search(self, nums: list[int], target: int) -> int:

        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= target <= nums[mid]:
                right = mid - 1

            elif nums[mid] <= target <= nums[right]:
                left = mid + 1

            elif nums[left] > nums[mid]:
                right = mid - 1

            else:  # nums[mid] >= nums[right]
                left = mid + 1

            return -1
