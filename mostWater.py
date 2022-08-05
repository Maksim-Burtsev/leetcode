class Solution:
    def maxArea(self, height: list[int]) -> int:

        if len(height) == 2:
            return min(height)

        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                left += 1
            else:
                area = (right - left) * height[right]
                right -= 1

            max_area = max(area, max_area)

        return max_area
