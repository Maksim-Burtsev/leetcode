from collections import Counter


class Solution:
    @staticmethod
    def minSetSize(arr: list[int]) -> int:
        counter_dict = Counter(arr)
        lenght = sum(counter_dict.values())
        res_count, res_freq = 0, 0
        for _, freq in counter_dict.most_common():
            res_count += 1
            res_freq += freq

            if res_freq >= lenght / 2:
                return res_count
