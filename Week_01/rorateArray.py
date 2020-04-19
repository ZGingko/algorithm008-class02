def rotateArray(nums,k):
    """
    189. 旋转数组
        给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

        示例 1:
            输入: [1,2,3,4,5,6,7] 和 k = 3
            输出: [5,6,7,1,2,3,4]
            解释:
                向右旋转 1 步: [7,1,2,3,4,5,6]
                向右旋转 2 步: [6,7,1,2,3,4,5]
                向右旋转 3 步: [5,6,7,1,2,3,4]
        
        示例 2:
            输入: [-1,-100,3,99] 和 k = 2
            输出: [3,99,-1,-100]
            解释: 
                向右旋转 1 步: [99,-1,-100,3]
                向右旋转 2 步: [3,99,-1,-100]
        说明:
            尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
            要求使用空间复杂度为 O(1) 的 原地 算法。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/rotate-array
    """
    n = len(nums)
    k = k % n
    if k < 0 or k > n:
        return
    # nums[:] = reversed(nums)
    # nums[:k] = reversed(nums[:k])
    # nums[k:] = reversed(nums[k:])
    reverse(nums,0,n-1)
    # print(nums)
    reverse(nums,0,k-1)
    # print(nums)
    reverse(nums,k,n-1)
    
def reverse(nums, start, end):
    while start<end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate(nums,k):
    n = len(nums)
    k = k % n
    if k < 0 or k > n:
        return
    cur, count = 0, 0
    curVal = nums[0]
    i = 0
    while count < n:
        cur = i
        curVal = nums[i]
        while True:
            next_ = (cur+k)%n
            curVal, nums[next_] = nums[next_], curVal
            cur = next_
            count += 1
            if cur == i:
                break
        i += 1


if __name__ == "__main__":
    nums, k = [1,2,3,4,5,6,7], 3
    # nums, k = [-1,-100,3,99], 2
    print(nums)
    rotate(nums, k)
    print(nums)