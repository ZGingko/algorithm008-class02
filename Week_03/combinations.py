from typing import List, Tuple, Dict

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:      
        """
        77. 组合
            给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
        """  
        nums = list(range(1, k + 1)) + [n + 1] # init first combination
        result, j = [], 0
        while j < k:
            # add current combination
            result.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1            
        return result
    
    def combine2(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # if the combination is done
            if len(curr) == k:  
                result.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        result = []
        backtrack()
        return result


if __name__ == "__main__":
    solution = Solution()
    n=4
    k=2
    print(solution.combine2(n,k))