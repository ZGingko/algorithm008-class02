from typing import List
import collections


class Solution:
    """
    212.单词搜索 II https://leetcode-cn.com/problems/word-search-ii/
    """
    # dx = [-1, 1, 0, 0]
    # dy = [0, 0, -1, 1]
    END_OF_WORD = "#"

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        if not words:
            return []
        self.result = set()
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[Solution.END_OF_WORD] = Solution.END_OF_WORD

        self.rows, self.cols = len(board), len(board[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)
        return list(self.result)

    def _dfs(self, board: List[List[str]], i: int, j: int, cur_word: str, cur_dict: dict) -> None:
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if Solution.END_OF_WORD in cur_dict:
            self.result.add(cur_word)
        tmp, board[i][j] = board[i][j], "@"
        # for k in range(4):
        #     x, y = i + Solution.dx[k], j + Solution.dy[k]
        for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = i + dx, j + dy
            if 0 <= x < self.rows and 0 <= y < self.cols and board[x][y] != "@" and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        79.单词搜索 https://leetcode-cn.com/problems/word-search/
        """
        self.rows = len(board)
        if self.rows == 0:
            return False
        self.cols = len(board[0])

        marked = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                # 对每一个格子都从头开始搜索
                if self.__search_word(board, word, 0, i, j, marked):
                    return True
        return False

    def __search_word(self, board, word, index, x, y, marked):
        # 先写递归终止条件
        if index == len(word) - 1:
            return board[x][y] == word[index]

        # 中间匹配了，再继续搜索
        if board[x][y] == word[index]:
            # 先占住这个位置，搜索不成功的话，要释放掉
            marked[x][y] = True
            for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_x = x + dx
                new_y = y + dy
                # 注意：如果这一次 search word 成功的话，就返回
                if (0 <= new_x < self.rows and 0 <= new_y < self.cols) and (not marked[new_x][new_y]) and \
                        self.__search_word(board, word, index + 1, new_x, new_y, marked):
                    return True
            marked[x][y] = False
        return False


if __name__ == "__main__":
    sol = Solution()
    words = ["oath", "pea", "eat", "rain"]
    board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
    ]
    print(sol.findWords(board, words))

    board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
    word = "ABCCED"

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    print(sol.exist(board, word))
