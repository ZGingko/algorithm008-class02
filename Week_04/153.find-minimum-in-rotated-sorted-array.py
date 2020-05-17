from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        153. 寻找旋转排序数组中的最小值
            假设按照升序排序的数组在预先未知的某个点上进行了旋转。
            ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

            请找出其中最小的元素。
            你可以假设数组中不存在重复元素。

            示例 1:
                输入: [3,4,5,1,2]
                输出: 1

            示例 2:
                输入: [4,5,6,7,0,1,2]
                输出: 0

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
        """
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1

        if nums[right] > nums[0]:  # 如果数组没有发生旋转，则第一个元素就是最小元素
            return nums[0]

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1  # 发生旋转的数组[0,mid]有序，则最小值肯定右侧区间中
            else:
                right = mid - 1


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(sol.findMin(nums))
