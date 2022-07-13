from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1, 1]]

        if numRows < 3:
            return triangle[:numRows]

        numRows = numRows - 1

        for i in range(1, numRows):
            tmp = [1]
            for j in range(len(triangle[i]) - 1):
                tmp.append(triangle[i][j] + triangle[i][j + 1])
            tmp.append(1)
            triangle.append(tmp)

        return triangle
