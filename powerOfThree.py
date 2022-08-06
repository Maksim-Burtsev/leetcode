class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power_list = {3**i for i in range(20)}
        return n in power_list
