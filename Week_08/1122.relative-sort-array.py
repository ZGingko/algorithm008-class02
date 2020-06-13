from typing import List


class Solution:
    """
    1122.数组的相对排序 https://leetcode-cn.com/problems/relative-sort-array/
    """
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        len1 = len(arr1)
        len2 = len(arr2)
        result = []
        temp = []
        for i in range(len2):
            for j in range(len1):
                if arr1[j] == arr2[i]:
                    result.append(arr1[j])
                    
        for j in range(len1):
            if arr1[j] not in set(result):
                temp.append(arr1[j])
                        
        return result + sorted(temp)


if __name__ == "__main__":
    sol  = Solution()
    arr1 = [28,6,22,8,44,17]
    arr2 = [22,28,8,6]
    print(sol.relativeSortArray(arr1, arr2))