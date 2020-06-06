from typing import List
import collections


class Solution:
    """
    127.单词接龙 https://leetcode-cn.com/problems/word-ladder/
    """
    def ladderLengthBFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord):
            return 0
        charSet = set("".join(wordList))
        wordSet = set(wordList)
        queue = collections.deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)
        result = 1

        while queue:
            count = len(queue)
            while count > 0:
                count -= 1
                current_word = queue.popleft()
                if current_word == endWord:
                    return result

                tmp = list(current_word)
                for i in range(len(tmp)):
                    old_ch = tmp[i]
                    for ch in charSet:
                        tmp[i] = ch
                        new_str = "".join(tmp)
                        if new_str not in visited and new_str in wordSet:
                            visited.add(new_str)
                            queue.append(new_str)
                    tmp[i] = old_ch
            result += 1
        return 0

    def ladderLength2DBFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        beginSet = {beginWord}
        endSet = {endWord}
        charSet = set("".join(wordList))

        wordSet = set(wordList)
        wordLen = len(beginWord)

        result = 1
        while beginSet:
            result += 1
            nextFront = set()
            for word in beginSet:
                for i in range(wordLen):
                    for ch in charSet:
                        if ch != word[i]:
                            newWord = word[:i] + ch + word[i+1:]
                            if newWord in endSet:
                                return result
                            if newWord in wordSet:
                                nextFront.add(newWord)
                                wordSet.remove(newWord)
            beginSet = nextFront
            if len(endSet) < len(beginSet):
                beginSet, endSet = endSet, beginSet
        return 0


if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.ladderLengthBFS(beginWord, endWord, wordList))
    print(sol.ladderLength2DBFS(beginWord, endWord, wordList))
