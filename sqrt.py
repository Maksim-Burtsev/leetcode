class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            middle = (left+right)//2
            if middle**2 == x:
                return middle
            if middle**2 < x:
                left = middle + 1
            else:
                right = middle - 1
        return middle-1


sol = Solution()
sol.mySqrt(12)
