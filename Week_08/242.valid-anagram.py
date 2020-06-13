class Solution:
    """
    242.有效的字母异位词 https://leetcode-cn.com/problems/valid-anagram/
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        base = ord('a')
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - base] += 1
            counter[ord(t[i]) - base] -= 1
        for c in counter:
            if c != 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    print(sol.isAnagram(s, t))