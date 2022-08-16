from collections import Counter


class Solution:
    @staticmethod
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        return [i[0] for i in Counter(nums).most_common(k)]

print(Solution.topKFrequent([1,1,1,2,2,3], 2))