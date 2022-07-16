class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        used_nums = set()

        while True:
            n = sum([int(i) ** 2 for i in str(n)])
            if n == 1:
                return True
            else:
                if n in used_nums:
                    return False
                used_nums.add(n)
