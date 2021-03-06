from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        221. 最大正方形
            在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

            示例:

            输入: 
                1 0 1 0 0
                1 0 1 1 1
                1 1 1 1 1
                1 0 0 1 0
            输出: 4

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/maximal-square
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    maxSide = max(maxSide, dp[i][j])
        return maxSide ** 2


if __name__ == "__main__":
    sol = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(sol.maximalSquare(matrix))