from typing import List


class Solution:
    """
    22.括号生成 https://leetcode-cn.com/problems/generate-parentheses/
    """
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    result.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': 
                    bal += 1
                else: 
                    bal -= 1
                if bal < 0: 
                    return False
            return bal == 0

        result = []
        generate([])
        return result

    def generateParenthesisDFS(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res

    def generateParenthesisDFS2(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right, n):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号已经使用的个数
            :param right: 右括号已经使用的个数
            :return:
            """
            if left == n and right == n:
                res.append(cur_str)
                return
            if left < right:
                return

            if left < n:
                dfs(cur_str + '(', left + 1, right, n)

            if right < n:
                dfs(cur_str + ')', left, right + 1, n)

        dfs(cur_str, 0, 0, n)
        return res

    def generateParenthesisDP(self, n: int) -> List[str]:
        if n == 0:
            return []

        dp = [None for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for s1 in left:
                    for s2 in right:
                        cur.append("(" + s1 + ")" + s2)
            dp[i] = cur
        return dp[n]

    def generateParenthesis(self, n: int) -> List[str]:
        dp = []
        dp.append([''])
        for i in range(1, n+1):
            temp = []
            for j in range(i):
                temp += ['(' + l + ')' + r for l in dp[j] for r in dp[i-1-j]]
            dp.append(temp)
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesisDFS(n))
    print(sol.generateParenthesisDFS2(n))
    print(sol.generateParenthesisDP(n))
    print(sol.generateParenthesis(n))

