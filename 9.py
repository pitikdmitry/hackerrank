class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows = len(A)
        cols = len(A[0])
        dp = [[-1 for j in range(cols)] for i in range(rows)]

        for col_i in range(0, cols):
            dp[0][col_i] = A[0][col_i]

        for row_i in range(1, rows):
            for col_i in range(0, cols):
                left_col_i = col_i - 1 if col_i > 0 else 0
                right_col_i = col_i + 1 if col_i < cols - 1 else cols - 1

                dp[row_i][col_i] = min(dp[row_i - 1][left_col_i], dp[row_i - 1][col_i], dp[row_i - 1][right_col_i]) \
                                   + A[row_i][col_i]

        return min(dp[rows - 1])


s = Solution()
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
res = s.minFallingPathSum(A)
print(res)
