from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        64. 最小路径和
            给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
            说明：每次只能向下或者向右移动一步。

            示例:
                输入:
                [
                  [1,3,1],
                  [1,5,1],
                  [4,2,1]
                ]
                输出: 7
                解释: 因为路径 1→3→1→1→1 的总和最小。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/minimum-path-sum
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[m - 1][n - 1]
        """
        1、刚开始时，即当i = 0, j = 0 时，其实就是起点， dp[i][j] = grid[i][j]；
        2、当只有左边是矩阵边界时： 只能从上面来，即当i = 0, j > 0， dp[i][j] = dp[i][j - 1] + grid[i][j]；
        3、当只有上边是矩阵边界时： 只能从左面来，即当i > 0, j = 0， dp[i][j] = dp[i - 1][j] + grid[i][j]；
        4、当左边和上边都不是矩阵边界时： 即当i > 0, j > 0, dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]；
        """


if __name__ == "__main__":
    sol = Solution()
    grid = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
        ]
    print(sol.minPathSum(grid))