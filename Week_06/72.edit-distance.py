class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        72. 编辑距离
            给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
            你可以对一个单词进行如下三种操作：
                插入一个字符
                删除一个字符
                替换一个字符             

            示例 1：
                输入：word1 = "horse", word2 = "ros"
                输出：3
                解释：
                    horse -> rorse (将 'h' 替换为 'r')
                    rorse -> rose (删除 'r')
                    rose -> ros (删除 'e')

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/edit-distance
        """
        m, n = len(word1), len(word2)
        
        # 有一个字符串为空串
        if n * m == 0:
            return n + m
        
        # DP 数组
        dp = [ [0] * (n + 1) for _ in range(m + 1)]
        
        # 边界状态初始化
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # 计算所有 DP 值
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                left_down = dp[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                dp[i][j] = min(left, down, left_down)
        
        return dp[m][n]
        """
        1. 动态规划

        2. 定义 dp[i][j]
            21. dp[i][j] 代表 word1 中前 i 个字符，变换到 word2 中前 j 个字符，最短需要操作的次数
            22. 需要考虑 word1 或 word2 一个字母都没有，即全增加/删除的情况，所以预留 dp[0][j] 和 dp[i][0]

        3. 状态转移
            31. 增，dp[i][j] = dp[i][j - 1] + 1
            32. 删，dp[i][j] = dp[i - 1][j] + 1
            33. 改，dp[i][j] = dp[i - 1][j - 1] + 1
            34. 按顺序计算，当计算 dp[i][j] 时，dp[i - 1][j] ， dp[i][j - 1] ， dp[i - 1][j - 1] 均已经确定了
            35. 配合增删改这三种操作，需要对应的 dp 把操作次数加一，取三种的最小
            36. 如果刚好这两个字母相同 word1[i - 1] = word2[j - 1] ，那么可以直接参考 dp[i - 1][j - 1] ，操作不用加一
        """


if __name__ == "__main__":
    sol = Solution()
    word1 = "horse"
    word2 = "ros"
    print(sol.minDistance(word1, word2))