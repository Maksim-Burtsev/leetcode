class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_ind = word.find(ch) + 1
        if ch_ind == -1:
            return word
        return word[:ch_ind][::-1] + word[ch_ind:]
