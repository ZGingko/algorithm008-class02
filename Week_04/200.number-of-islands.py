from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
            岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
            此外，你可以假设该网格的四条边均被水包围。             

            示例 1:
                输入:
                    11110
                    11010
                    11000
                    00000
                输出: 1

            示例 2:
                输入:
                    11000
                    11000
                    00100
                    00011
                输出: 3
                解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/number-of-islands
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])        
        result = 0
        def DFS(grid,x,y):
            if x<0 or x>=m or y<0 or y>=n or grid[x][y]!='1':
                return
            grid[x][y] = 0
            DFS(grid,x-1,y)
            DFS(grid,x+1,y)
            DFS(grid,x,y-1)
            DFS(grid,x,y+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    DFS(grid,i,j)
        return result


if __name__ == "__main__":
    sol = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(sol.numIslands(grid))
