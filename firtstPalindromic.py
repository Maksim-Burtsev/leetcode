class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if word[::-1] == word:
                return word
        
        return ""