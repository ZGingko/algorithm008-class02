import bisect
from typing import List


class Solution:
    """
    493.翻转对 https://leetcode-cn.com/problems/reverse-pairs/
    """

    def reversePairs(self, nums: List[int]) -> int:
        # binary search
        if nums == []:
            return 0
        ans, arr = 0, []
        for num in reversed(nums):
            ans += bisect.bisect_left(arr, num)
            bisect.insort(arr, num * 2)  # O(N) but actually it's very fast
        return ans

    def reversePairs2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, left, right):
        if left >= right:
            return 0
        
        mid = (left + right) >> 1 # left + (right - left) // 2
        result = self.mergeSort(nums, left, mid) + self.mergeSort(nums,  mid + 1, right)
        cache = [None] * (right - left + 1)
        i = left
        t = left
        c = 0
        j = mid + 1
        while j <= right:
            while i <= mid and nums[i] <= 2*nums[j]:
                i += 1
            while t <= mid and nums[t] < nums[j]:
                cache[c] = nums[t]
                c += 1
                t += 1
            cache[c] = nums[j]
            result += mid - i + 1
            j += 1
            c += 1
        while t <= mid:
            cache[c] = nums[t]
            c += 1
            t += 1
        print(cache)
        print(nums, left, right)
        nums[left:right+1] = cache[0:]
        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [2,4,3,5,1] # [1, 2, 3, 3, 1]
    print(sol.reversePairs2(nums))
