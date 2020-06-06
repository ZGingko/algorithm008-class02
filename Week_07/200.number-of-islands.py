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
    200. 岛屿数量 https://leetcode-cn.com/problems/number-of-islands/
    """
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        def dfs(grid, x, y):
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1' and not visited[x][y]:
                visited[x][y] = True
                for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    dfs(grid, x + dx, y + dy)

        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(grid, i, j)
                    result += 1
        return result

    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        # 特判
        if rows == 0:
            return 0
        cols = len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        result = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
        for i in range(rows):
            for j in range(cols):
                # 只要是陆地，且没有被访问过的，就可以使用 BFS 发现与之相连的陆地，并进行标记
                if not visited[i][j] and grid[i][j] == '1':
                    # result 可以理解为连通分量，你可以在广度优先遍历完成以后，再计数，
                    # 即这行代码放在【位置 1】也是可以的
                    result += 1
                    queue = collections.deque()
                    queue.append((i, j))
                    # 注意：这里要标记上已经访问过
                    visited[i][j] = True
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        # 得到 4 个方向的坐标
                        for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            new_x, new_y = cur_x + dx, cur_y + dy
                            # 如果不越界、没有被访问过、并且还要是陆地，我就继续放入队列，放入队列的同时，要记得标记已经访问过
                            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and grid[new_x][new_y] == '1':
                                queue.append((new_x, new_y))
                                # 【特别注意】在放入队列以后，要马上标记成已经访问过，语义也是十分清楚的：反正只要进入了队列，你迟早都会遍历到它
                                # 而不是在出队列的时候再标记
                                # 【特别注意】如果是出队列的时候再标记，会造成很多重复的结点进入队列，造成重复的操作，这句话如果你没有写对地方，代码会严重超时的
                                visited[new_x][new_y] = True
                    # 【位置 1】
        return result

    def numIslands(self, grid: List[List[str]]) -> int:
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

    def numIslandsUF(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        # 特判
        if rows == 0:
            return 0
        cols = len(grid[0])

        def get_index(x, y):
            return x * cols + y

        # 注意：我们不用像 DFS 和 BFS 一样，4 个方向都要尝试，只要看一看右边和下面就可以了
        directions = [(1, 0), (0, 1)]
        # 多开一个空间，把水域 "0" 都归到这个虚拟的老大上
        dummy_node = rows * cols

        # 多开的一个空间就是那个虚拟的空间
        uf = UnionFind(dummy_node + 1)
        for i in range(rows):
            for j in range(cols):
                # 如果是水域，都连到那个虚拟的空间去
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                if grid[i][j] == '1':
                    # 向下向右如果都是陆地，即 "1"，就要合并一下
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < rows and new_y < cols and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))
        # 不要忘记把那个虚拟结点减掉
        return uf.get_count() - 1


if __name__ == "__main__":
    sol = Solution()
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(sol.numIslandsDFS(grid))
    print(sol.numIslandsBFS(grid))
    print(sol.numIslandsUF(grid))
    print(sol.numIslands(grid))
