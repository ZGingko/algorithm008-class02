from typing import List


class Solution:
    """
    56.合并区间 https://leetcode-cn.com/problems/merge-intervals/
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # 按照区间左值排序
        n = len(intervals)
        result = []
        for interval in intervals:
            # 结果数组为空，或者结果数组中的最后区间右值小于当前区间的左值，则直接添加当前区间到结果数组中
            if not result or result[-1][1] < interval[0]: 
                result.append(interval)
            else:
                # 反之将当前区间合并至结果数组的最后区间
                result[-1][1] = max(result[-1][1], interval[1])
        return result


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    print(sol.merge(intervals))