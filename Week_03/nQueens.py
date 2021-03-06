class Solution:
    def solveNQueens(self, n):
        """
        51.N皇后
            n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
            给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
            每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
            PS：皇后可以攻击同一行、同一列、左上左下右上右下四个方向的任意单位。
            示例:
                输入: 4
                输出: [
                    [".Q..",  // 解法 1
                    "...Q",
                    "Q...",
                    "..Q."],

                    ["..Q.",  // 解法 2
                    "Q...",
                    "...Q",
                    ".Q.."]
                ]
                解释: 4 皇后问题存在两个不同的解法。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/n-queens
        """
        if n < 1:
            return []

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
        print(result)
        return [["."*i + "Q"+"."*(n-i-1) for i in sol] for sol in result]

    
    def totalNQueens(self, n):
        if n<1:
            return []
        self.count = 0
        self.result = []
        self.DFS(n,0,0,0,0,[])
        print(self.result)
        return self.count
    
    def DFS(self,n,row,cols,pie,na,queens):
        # recursion terminator
        if row >= n:
            self.count += 1
            self.result.append(queens)
            return

        bits = (~(cols | pie | na)) & ((1 << n) - 1) # 得到当前所有的空位
        
        while bits:
            p = bits & -bits  # 取得最低位的1
            self.DFS(n,row+1, cols | p,(pie|p) << 1, (na|p) >> 1,queens+[p])
            bits = bits & (bits - 1) # 去掉最低位的1
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))
    print(sol.totalNQueens(4))
    