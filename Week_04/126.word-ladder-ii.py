from typing import List
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
            给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

            每次转换只能改变一个字母。
            转换过程中的中间单词必须是字典中的单词。
            说明:
                如果不存在这样的转换序列，返回一个空列表。
                所有单词具有相同的长度。
                所有单词只由小写字母组成。
                字典中不存在重复的单词。
            你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

            示例 1:
                输入:
                    beginWord = "hit",
                    endWord = "cog",
                    wordList = ["hot","dot","dog","lot","log","cog"]

                输出:
                    [
                        ["hit","hot","dot","dog","cog"],
                          ["hit","hot","lot","log","cog"]
                    ]

            示例 2:
                输入:
                    beginWord = "hit"
                    endWord = "cog"
                    wordList = ["hot","dot","dog","lot","log"]

                输出: []

                解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/word-ladder-ii
        """
        wordList.append(beginWord)
        # 构建具有邻接关系的桶
        buckets = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                match = word[:i] + '_' + word[i+1:]
                buckets[match].append(word)
        # BFS遍历
        preWords = collections.defaultdict(list)  # 前溯词列表
        toSeen = collections.deque([(beginWord, 1)])  # 待遍历词及深度列表
        beFound = {beginWord: 1}  # 已探测词词列表
        while toSeen:
            curWord, level = toSeen.popleft()
            for i in range(len(beginWord)):
                match = curWord[:i] + '_' + curWord[i+1:]
                for word in buckets[match]:
                    if word not in beFound:
                        beFound[word] = level+1
                        toSeen.append((word, level+1))
                    if beFound[word] == level+1:  # 当前深度等于该词首次遍历深度，则仍应加入前溯词列表
                        preWords[word].append(curWord)
            # 已搜索到目标词，且完成当前层遍历
            if endWord in beFound and level+1 > beFound[endWord]:
                break
        # 列表推导式输出结果
        if endWord in beFound:
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = [[word] + r for r in res for word in preWords[r[0]]]
            return res
        else:
            return []


if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log","cog"]
    print(sol.findLadders(beginWord, endWord, wordList))
