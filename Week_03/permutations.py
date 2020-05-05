from typing  import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        46. 全排列
            给定一个 没有重复 数字的序列，返回其所有可能的全排列。
        """
        n = len(nums)
        result = []
        def backtrack(first = 0):
            if first == n:  
                result.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]  
                      
        backtrack()
        return result

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        47. 全排列 II
            给定一个可包含重复数字的序列，返回所有不重复的全排列。
        """
        def backtrack(sol, nums, check):
            if len(sol) == len(nums):
                self.result.append(sol)
                return            
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                    continue
                check[i] = 1
                backtrack(sol+[nums[i]], nums, check)
                check[i] = 0

        nums.sort()
        self.result = []
        check = [0 for i in range(len(nums))]
        
        backtrack([], nums, check)
        return self.result


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3]
    print(solution.permute(nums))