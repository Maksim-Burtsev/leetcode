class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0

        while dividend >= divisor:

            temp_div, k = divisor, 1

            while dividend >= temp_div:

                dividend -= temp_div

                res += k

                k = k << 1  # *2

                temp_div = temp_div << 1  # *2

        if not positive:
            res = -res

        return min(max(-2147483648, res), 2147483647)
