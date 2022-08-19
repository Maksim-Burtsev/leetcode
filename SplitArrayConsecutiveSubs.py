from collections import defaultdict, Counter


class Solution:
    @staticmethod
    def isPossible(nums: list[int]) -> bool:
        counter = Counter(nums)
        seq = defaultdict(int)

        for num in nums:
            if not counter[num] > 0:
                continue

            if seq[num - 1] > 0:
                seq[num - 1] -= 1
                seq[num] += 1
                counter[num] -= 1

            else:
                if not (counter[num + 1] > 0 and counter[num + 2] > 0):
                    return False
                counter[num] -= 1
                counter[num + 1] -= 1
                counter[num + 2] -= 1
                seq[num + 2] += 1

        return True


print(Solution.isPossible([1, 2, 3, 3, 4, 5]))
