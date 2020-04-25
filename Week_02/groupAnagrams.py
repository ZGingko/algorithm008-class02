class Solution:
    def groupAnagrams(self, strs:list) -> list:
        """
        49. 字母异位词分组
            给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

            示例:
                输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
                输出:
                [
                    ["ate","eat","tea"],
                    ["nat","tan"],
                    ["bat"]
                ]

            说明：
                所有输入均为小写字母。
                不考虑答案输出的顺序。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/group-anagrams
        """
        if not strs:
            return []
        counter = {}
        for i in range(len(strs)):
            item = sorted(strs[i])
            if str(item) not in counter:
                counter[str(item)] = [strs[i]]
            else:
                counter[str(item)].append(strs[i])
        result = []
        for item in counter:
            result.append(counter[item])
        return result

    def groupAnagrams1(self,strs:list) -> list:
        """字典计数法"""
        if not strs:
            return []
        result = {}
        for w in strs:
            key = tuple(sorted(w))
            result[key] = result.get(key, []) + [w]
        return list(result.values())

    def groupAnagrams2(self,strs):
        """26个小写字母计数法"""
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


if __name__ == "__main__":
    solution = Solution()
    strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams2(strs))