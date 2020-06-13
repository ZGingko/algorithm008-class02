class Solution:
    """
    191.位1的个数 https://leetcode-cn.com/problems/number-of-1-bits/
    """
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n = n & (n-1)
            result += 1
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(4))