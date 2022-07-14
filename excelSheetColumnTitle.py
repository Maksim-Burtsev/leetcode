import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        alphabet = {i: letter for i, letter in enumerate(string.ascii_uppercase)}

        ans = ""
        while columnNumber:
            ans += alphabet[(columnNumber - 1) % 26]
            columnNumber = (columnNumber - 1) // 26
        return ans[::-1]


sol = Solution()
sol.convertToTitle(701)
