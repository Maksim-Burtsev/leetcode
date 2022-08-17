import string

a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
code = {letter:a[i] for i, letter in enumerate(string.ascii_lowercase)}

class Solution:

    @staticmethod
    def uniqueMorseRepresentations(words: list[str]) -> int:
        res = set(''.join([code[i] for i in word]) for word in words)
        return len(res)
