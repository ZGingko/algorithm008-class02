from typing import List
import collections

class Solution:
    """
    51.N皇后 https://leetcode-cn.com/problems/n-queens/
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queens+[q], xy_dif + [p-q], xy_sum+[p+q])
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


if __name__ == "__main__":
    sol = Solution() 