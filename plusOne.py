from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = 1

        for i in range(len(digits) - 1, 0, -1):
            digits[i] = digits[i] + tmp
            if digits[i] >= 10:
                tmp = 1
                digits[i] = digits[i] % 10
            else:
                tmp = 0
                break

        digits[0] = digits[0] + tmp
        if digits[0] == 10:
            digits[0] = digits[0] % 10
            digits.insert(0, 1)
        return digits
