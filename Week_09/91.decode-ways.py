class Solution:
    """
    91.解码方法 https://leetcode-cn.com/problems/decode-ways/
    """
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0] == '0':
            return 0
        pre = 1
        cur = 1
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    cur = pre
                else:
                    return 0
            else:
                if s[i-1] == '1' or (s[i-1] == '2' and int(s[i]) >= 1 and int(s[i]) <= 6):
                    cur += pre
                else:
                    cur = cur
            pre = tmp
        return cur

if __name__ == "__main__":
    sol = Solution()
    s = "12"
    print(sol.numDecodings(s))
        