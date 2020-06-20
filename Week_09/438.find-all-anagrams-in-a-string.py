from typing import List

class Solution:
    """
    438.找到字符串中所有字母异位词 https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "cbaebabacd" 
    p = "abc"
    print(sol.findAnagrams(s, p))