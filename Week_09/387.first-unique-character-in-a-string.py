import collections


class Solution:
    """
    387.字符串中的第一个唯一字符 https://leetcode-cn.com/problems/first-unique-character-in-a-string/
    """

    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


if __name__ == "__main__":
    sol = Solution()
    s = "loveleetcode"
    print(sol.firstUniqChar(s))
