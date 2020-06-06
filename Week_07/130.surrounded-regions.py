from typing import List
import collections


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def get_count(self):
        return self.count

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        if self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[q_root] = p_root
            self.rank[p_root] += 1

        self.count -= 1


class Solution:
    """
    130.被围绕的区域 https://leetcode-cn.com/problems/surrounded-regions/
    """
    def solveDFS(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i, tmp_j = i + x, j + y
                if 1 <= tmp_i < rows and 1 <= tmp_j < cols and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)

        for j in range(cols):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)

        for i in range(rows):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][cols-1] == "O":
                dfs(i, cols - 1)

        for i in range(rows):
            for j in range(cols):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"

    def solveBFS(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])

        def bfs(i, j):
            queue = collections.deque()
            queue.appendleft((i, j))
            while queue:
                i, j = queue.pop()
                if 0 <= i < rows and 0 <= j < cols and board[i][j] == "O":
                    board[i][j] = "B"
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.appendleft((i + x, j + y))

        for j in range(cols):
            # 第一行
            if board[0][j] == "O":
                bfs(0, j)
            # 最后一行
            if board[rows - 1][j] == "O":
                bfs(rows - 1, j)

        for i in range(rows):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][cols - 1] == "O":
                bfs(i, cols - 1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"

    def solveUF(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        root = {}
        def find(x):
            root.setdefault(x, x)
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            root[find(y)] = find(x)

        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        dummy = rows * cols
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        union(i * cols + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * cols + j, (i + x) * cols + (j + y))
        for i in range(rows):
            for j in range(cols):
                if find(dummy) == find(i * cols + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


if __name__ == "__main__":
    sol = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol.solveBFS(board)
    print(board)