class Solution:
    @staticmethod
    def partitionLabels(s: str) -> list[int]:
        index_dict = {letter: ind for ind, letter in enumerate(s)}

        res = []
        start, end = 0, 0

        while start < len(s):
            end = index_dict[s[start]]

            i = start + 1
            while i < end:
                if index_dict[s[i]] > end:
                    end = index_dict[s[i]]
                i += 1
            res.append(end+1-start)
            start = end + 1

        return res
