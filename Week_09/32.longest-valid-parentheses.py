class Solution:
    """
    32.最长有效括号 https://leetcode-cn.com/problems/longest-valid-parentheses/
    """

    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        result = 0
        n = len(s)
        tmp = [-1]
        for i in range(n):
            if s[i] == ')' and len(tmp) > 1 and s[tmp[-1]] == '(':
                tmp.pop()
                result = max(result, i - tmp[-1])
            else:
                tmp.append(i)
        return result


if __name__ == "__main__":
    sol = Solution()
    s = "((())"
    print(sol.longestValidParentheses(s))
