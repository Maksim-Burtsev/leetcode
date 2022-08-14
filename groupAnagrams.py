# class Solution:
#     @staticmethod
#     def groupAnagrams(strs: list[str]) -> list[list[str]]:
#         if len(strs) < 2:
#             return [strs]
#         res = []
#         sorted_strs = [''.join(sorted(i)) for i in strs]

#         for i, str_ in enumerate(sorted_strs):
#             if str_ is not None:
#                 group = [strs[i], ]
#                 for j in range(i+1, len(strs)):
#                     if sorted_strs[j] == str_:
#                         group.append(strs[j])
#                         sorted_strs[j] = None
#                 res.append(group)
#         return res

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for str_ in strs:
            res["".join(sorted(str_))].append(str_)

        return list(res.values())
