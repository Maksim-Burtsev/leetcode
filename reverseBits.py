class Solution:
    def reverseBits(self, n: int) -> int:
        bit_str = "{0:032b}".format(n)
        return int(bit_str[::-1], base=2)
