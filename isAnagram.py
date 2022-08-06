from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s).items() == Counter(t).items()

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))