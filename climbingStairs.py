class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2

        fib_array = [1, 1]

        for i in range(1, n):
            fib_array.append(fib_array[i - 1] + fib_array[i])

        return fib_array[-1]
