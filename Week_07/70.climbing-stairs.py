class Solution:
    """
    70.爬楼梯 https://leetcode-cn.com/problems/climbing-stairs/
    """
    def climbStairs(self, n: int) -> int:
        """
        状态表示：dp[i]:表示到第i个台阶的走法数量
        状态转移：dp[i] = dp[i-1] + dp[i-2], i >= 2
        边界情况：dp[0] = 1, dp[1] = 1  
        """
        if n <= 1:
            return 1
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs2(self, n:int) -> int:
        if n < 3:
            return n
        a, b = 1, 2
        i = 3
        for i in range(3, n+1):
            a, b = b, a+b
        return b


if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.climbStairs(n))
    print(sol.climbStairs2(n))