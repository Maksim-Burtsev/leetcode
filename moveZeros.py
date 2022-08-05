class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        ptr = 1
        flag = False
        for i in range(len(nums)):
            if nums[i] == 0:
                ptr = i+1 if ptr < i else ptr
                for j in range(ptr, len(nums)):
                    if nums[j] != 0:
                        flag = True
                        ptr = j
                        break
                if flag:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    flag = False
        return nums

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 

        ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                ptr +=1

        return nums

sol = Solution()
sol.moveZeroes([0,])
