class Solution(object):
    """
    242. 有效的字母异位词
        给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
        所谓字母异位词：即两个字符串包含的字母及个数都相同，只是各字母相对位置不一样

        示例 1:
            输入: s = "anagram", t = "nagaram"
            输出: true

        示例 2:
            输入: s = "rat", t = "car"
            输出: false

        说明:
            你可以假设字符串只包含小写字母。

        进阶:
        如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/valid-anagram
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """直接排序法"""
        return len(s) == len(t) and sorted(s) == sorted(t)

    
    def isAnagram1(self, s: str, t: str) -> bool:
        """哈希表计数法"""
        if len(s)!=len(t):
            return False
        tmp = {}
        for x in s:
            if x not in tmp:
                tmp[x] = 1
            else:
                tmp[x] += 1
        for x in t:
            if x not in tmp:
                return False
            tmp[x] -=1
        for v in tmp:
            if tmp[v] != 0:
                return False
        return True
    
    def isAnagram2(self,s:str,t:str) -> bool:
        """26英文字符计数法"""
        if len(s)!=len(t):
            return False
        base = ord('a')
        counter = [0]*26
        for i in range(len(s)):
            counter[ord(s[i])-base] += 1
            counter[ord(t[i])-base] -= 1
        for c in counter:
            if c != 0:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram2(s,t))