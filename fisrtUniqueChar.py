from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, j in Counter(s).items():
            if j == 1:
                return s.find(i)
        return -1


solution = Solution()
print(solution.firstUniqChar("loveleetcode"))