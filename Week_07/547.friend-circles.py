from typing import List
import collections


class Solution:
    """
    547.朋友圈 https://leetcode-cn.com/problems/friend-circles/
    """
    def findCircleNumDFS(self, M: List[List[int]]) -> int:
        visited = [0] * len(M)
        result = 0

        def dfs(M, visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(M, visited, j)

        for i in range(len(M)):
            if visited[i] == 0:
                dfs(M, visited, i)
                result += 1
        return result

    def findCircleNumBFS(self, M: List[List[int]]) -> int:
        visited = [0] * len(M)
        result = 0
        queue = collections.deque()
        for i in range(len(M)):
            if visited[i] == 0:
                queue.append(i)
                while queue:
                    cur = queue.popleft()
                    visited[cur] = 1
                    for j in range(len(M)):
                        if M[cur][j] == 1 and visited[j] == 0:
                            queue.append(j)
                result += 1
        return result

    def findCircleNumUF(self, M: List[List[int]]) -> int:
        def find(root: List[int], i: int):
            if root[i] == -1:
                return i
            return find(root, root[i])

        def union(root: List[int], x: int, y: int):
            rootx = find(root, x)
            rooty = find(root, y)
            if rootx != rooty:
                root[rootx] = rooty

        n = len(M)
        root = [-1] * n
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1 and i != j:
                    union(root, i, j)

        result = 0
        for i in range(len(root)):
            if root[i] == -1:
                result += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    M = [
            [1,1,0],
            [1,1,0],
            [0,0,1]
        ]
    print(sol.findCircleNumDFS(M))
    print(sol.findCircleNumBFS(M))
    print(sol.findCircleNumUF(M))
