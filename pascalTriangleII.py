from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1], [1, 1]]

        if rowIndex < 2:
            return triangle[rowIndex]

        for i in range(1, rowIndex):
            tmp = [1]
            for j in range(len(triangle[i]) - 1):
                tmp.append(triangle[i][j] + triangle[i][j + 1])
            tmp.append(1)

            triangle.append(tmp)

        return triangle[rowIndex]
