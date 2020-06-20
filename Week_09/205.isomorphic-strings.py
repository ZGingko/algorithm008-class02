class Solution:
    """
    205.同构字符串 https://leetcode-cn.com/problems/isomorphic-strings/
    """
    def isIsomorphic(self, s, t):
        if not s:
            return True
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "egg"
    t = "pdd"
    print(sol.isIsomorphic(s, t))