import collections

class Solution:
    def majorityElement(self, nums) -> int:
        """
        169. 多数元素
            给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
            你可以假设数组是非空的，并且给定的数组总是存在多数元素。

            示例 1:
                输入: [3,2,3]
                输出: 3
                示例 2:

                输入: [2,2,1,1,1,2,2]
                输出: 2

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/majority-element
        """
        tmp = {}
        for num in nums:
            tmp[num] = tmp.get(num, 0)+1
            if tmp[num] > len(nums)//2:
                return num
        return None

    def majorityElement2(self, nums):
        """
        利用python库函数求解
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement3(self, nums):
        """
        排序法
        """
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement4(self, nums, low=0, hi=None):
        """
        分治法
        """
        def majority_element_rec(low, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if low == hi:
                return nums[low]

            # recurse on left and right halves of this slice.
            mid = (hi-low)//2 + low
            left = majority_element_rec(low, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(low, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(low, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)

if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,1,1,1,2,2]
    print(sol.majorityElement(nums))