from typing import List


class Solution:
    """
    300.最长上升子序列 https://leetcode-cn.com/problems/longest-increasing-subsequence/
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        result = 0
        for i in range(len(dp)):
            result = max(result, dp[i])
        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(sol.lengthOfLIS(nums))