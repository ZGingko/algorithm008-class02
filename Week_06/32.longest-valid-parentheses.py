class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        32. 最长有效括号
            给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

            示例 1:
                输入: "(()"
                输出: 2
                解释: 最长有效括号子串为 "()"

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/longest-valid-parentheses 
        """
        n = len(s)
        if n == 0: return 0
        
        dp = [0] * n
        result = 0
        for i in range(n):
            if i > 0 and s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif s[i-1] == ')' and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    
                result = max(result, dp[i])        
        return result
        """
        1、定义状态数组：dp[i]表示以下标为i的字符结尾的最长有效子串的长度
        2、状态转移方程：
            1）s[i] == ')' 且 s[i-1] == '(',即形如“......()”，可以推导出：dp[i] = dp[i-2] + 2
            2）s[i] == ')' 且 s[i-1] == ')',即形如“......))”，可以推导出：如果 s[i-dp[i-1]-1] = '(',那么
                dp[i] = dp[i-1] + 2 + dp[i-dp[i-1] - 2]
        """


if __name__ == "__main__":
    sol = Solution()
    s =  ")()())"
    print(sol.longestValidParentheses(s))