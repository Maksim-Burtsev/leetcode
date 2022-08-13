from itertools import permutations


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # return [list(i) for i in permutations(nums)]
        res = []
        visited = set()
        self.helper(res, visited, [], nums)
        return res

    def helper(self, res: list, visited: set, combibation: list, nums: list):
        if len(combibation) == len(nums):
            res.append(combibation)
        
        for i, num in enumerate(nums):
            if i not in visited:
                visited.add(i)
                self.helper(res, visited, combibation+[num,], nums)
                visited.remove(i)
                
