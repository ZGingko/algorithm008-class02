class Solution:
    """
    917.仅仅反转字母 https://leetcode-cn.com/problems/reverse-only-letters/
    """
    def reverseOnlyLetters(self, S: str) -> str:
        left, right = 0, len(S) - 1
        temp = list(S)
        while left <= right:
            while left < right and not temp[left].isalpha():
                left += 1
            while left < right and not temp[right].isalpha():
                right -= 1
            temp[left], temp[right] = temp[right], temp[left]
            left, right = left + 1, right - 1

        return "".join(temp)

if __name__ == "__main__":
    sol = Solution()
    S = "ab-cd" # "a-bC-dEf-ghIj"
    print(sol.reverseOnlyLetters(S))
