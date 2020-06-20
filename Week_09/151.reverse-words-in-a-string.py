import collections

class Solution:
    # def reverseWords(self, s: str) -> str:
    #     # p = re.compile(r"\b");
    #     l = s.split()
    #     return " ".join(reversed(l))
    
    def reverseWords(self, s: str) -> str:
        """
        151.翻转字符串里的单词 https://leetcode-cn.com/problems/reverse-words-in-a-string/
        """
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        d, word = collections.deque(), []
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1

        d.appendleft(''.join(word))     
        return ' '.join(d)      

    def reverseWordsIII(self, s: str) -> str:
        """
        557.反转字符串中的单词 III https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
        """
        # return " ".join(word[::-1] for word in s.split(" "))
        l = s.split()
        for i in range(len(l)):
            l[i] = ''.join(reversed(list(l[i])))
        return ' '.join(l)

if __name__ == "__main__":
    sol = Solution()
    s = "the sky is  blue"
    print(sol.reverseWords(s))
    print(sol.reverseWordsIII(s))
