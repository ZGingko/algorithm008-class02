class Solution:
    def numDecodings(self, s: str) -> int:
        """
        91. 解码方法
            一条包含字母 A-Z 的消息通过以下方式进行了编码：
                'A' -> 1
                'B' -> 2
                ...
                'Z' -> 26
            给定一个只包含数字的非空字符串，请计算解码方法的总数。

            示例 1:
                输入: "12"
                输出: 2
                解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

            示例 2:
                输入: "226"
                输出: 3
                解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/decode-ways
        """
        if len(s) == 0: return 0
        if s[0] == '0': return 0
        pre = 1 # dp[-1]
        cur = 1 # dp[0]
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == '0':
                if s[i-1] =='1' or s[i-1] == '2': # 后两位 一起解码‘10’或‘20’ 
                    cur = pre
                else:
                    return 0
            else:
                if s[i-1] == '1' or (s[i-1] == '2' and int(s[i]) >= 1 and int(s[i]) <= 6): # 后两位取值11-26
                    cur += pre
                else: # 后两位不在11-26之间，必须分开解码
                    cur = cur
            pre = tmp
        return cur


if __name__ == "__main__":
    sol = Solution()
    s = "2264"
    print(sol.numDecodings(s))