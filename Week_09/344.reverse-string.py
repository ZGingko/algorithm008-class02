from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        344.反转字符串 https://leetcode-cn.com/problems/reverse-string/
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    def reverseStr(self, s: str, k: int) -> str:
        """
        541.反转字符串II https://leetcode-cn.com/problems/reverse-string-ii/
        """
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)


if __name__ == "__main__":
    sol = Solution()
    s = ["h", "e", "l", "l", "o"]
    print(s)
    sol.reverseString(s)
    print(s)

    ss = "abcdefg"
    k = 2
    print(sol.reverseStr(ss,k))
