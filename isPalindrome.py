class Solution:
    def isPalindrome(self, s: str) -> bool:
        charactes = "".join([str(i) for i in s if i.isalpha() or i.isdigit()]).lower()
        return charactes == charactes[::-1]
