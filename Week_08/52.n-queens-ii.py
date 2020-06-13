class Solution:
    """
    52.N皇后 II https://leetcode-cn.com/problems/n-queens-ii/
    """
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return []
        
        def DFS(row, cols, xy_dif, xy_sum):
            if row >= n:
                self.result += 1
                return 
            
            bits = (~(cols|xy_dif|xy_sum)) & ((1 << n) - 1) # 得到当前所有的空位
            print("row:{}, cols:{}, xy_dif:{}, xy_sum:{}, bits:{}".format(bin(row), bin(cols), bin(xy_dif), bin(xy_sum), bin(bits)))
            
            while bits:
                p = bits & -bits # 取到最低位的1
                bits = bits & (bits - 1) # 表示在p位置上放入皇后
                DFS(row + 1, cols | p, (xy_dif | p) << 1, (xy_sum | p) >> 1)
                # 不需要revert cols, xy_dif, xy_sum
        
        self.result = 0
        DFS(0, 0, 0, 0)
        return self.result

if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.totalNQueens(n))