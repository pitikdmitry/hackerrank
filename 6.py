# rotate 2d matrix


class Solution:
    def rotate(self, matrix: []) -> None:
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        res = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
        for row_i in range(rows):
            for col_j in range(cols):
                el = matrix[row_i][col_j]
                new_i = col_j
                new_j = rows - row_i - 1
                res[new_i][new_j] = el

        for row_i in range(rows):
            for col_j in range(cols):
                matrix[row_i][col_j] = res[row_i][col_j]


s = Solution()
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
s.rotate(matrix)
print(matrix)
