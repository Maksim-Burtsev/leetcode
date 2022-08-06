from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_count, nums2_count = Counter(nums1), Counter(nums2)   


        interspect_dict = {}
        for val in nums1_count.keys():
            if nums2_count.get(val):
               interspect_dict[val] = min(nums1_count[val], nums2_count[val]) 

        res = []
        for i, j in interspect_dict.items():
            for _ in range(j):
                res.append(i)

        return res

sol = Solution()
sol.intersect([1, 2, 2, 1, 3], [2, 2, 3])
