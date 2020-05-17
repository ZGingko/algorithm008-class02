from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        33. 搜索旋转排序数组
            假设按照升序排序的数组在预先未知的某个点上进行了旋转。
            ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
            搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

            你可以假设数组中不存在重复的元素。
            你的算法时间复杂度必须是 O(log n) 级别。

            示例 1:
                输入: nums = [4,5,6,7,0,1,2], target = 0
                输出: 4
            示例 2:
                输入: nums = [4,5,6,7,0,1,2], target = 3
                输出: -1

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
        """
        left,right = 0,len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[0] <= nums[mid] and (target > nums[mid] or target < nums[0]):
                left = mid + 1
            elif target > nums[mid] and target < nums[0]:
                left = mid + 1
            else:
                right = mid
        return left if (left == right and nums[left]==target) else -1


if __name__ == "__main__":
    sol = Solution()
    nums, target = [4,5,6,7,0,1,2], 0
    print(sol.search(nums,target))