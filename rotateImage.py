class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        j = len(matrix)-1
        while j > len(matrix)-1-j:
            for i in range(len(matrix)):
                matrix[i][j], matrix[i][len(matrix)-1-j] = matrix[i][len(matrix)-1-j], matrix[i][j]
            j -= 1

        return matrix
solution = Solution()
solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])