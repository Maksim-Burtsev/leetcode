from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m  = len(matrix), len(matrix[0])
        i_list, j_list = [], []

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    i_list.append(i)
                    j_list.append(j)

        i_list = set(i_list)
        j_list = set(j_list)

        for i in i_list:
            for j in range(m):
                matrix[i][j] = 0

        for j in j_list:
            for i in range(n):
                matrix[i][j] = 0