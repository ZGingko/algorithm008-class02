class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        面试题49. 丑数
            我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
            示例:
                输入: n = 10
                输出: 12
                解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
            
            说明:  
                1 是丑数。
                n 不超过1690。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/chou-shu-lcof
        """
        if n > 1690:
            raise ValueError("参数错误，超过规定值上限：1690")
        dp, p2, p3, p5 = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: 
                p2 += 1
            if dp[i] == n3: 
                p3 += 1
            if dp[i] == n5: 
                p5 += 1
        return dp[-1]
    
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber2(self, n):
        return self.ugly[n-1]

    def nthUglyNumber3(self, n):
        import heapq
        q2, q3, q5 = [2], [3], [5]
        ugly = 1
        for u in heapq.merge(q2, q3, q5):
            if n == 1:
                return ugly
            if u > ugly:
                ugly = u
                n -= 1
                q2 += 2 * u,
                q3 += 3 * u,
                q5 += 5 * u,

if __name__ == "__main__":
    solution = Solution()
    k = 5
    print("第 %d 个丑数: " % k, end = " ")
    print(solution.nthUglyNumber(k))