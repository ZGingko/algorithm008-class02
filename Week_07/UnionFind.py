class UnionFind:
    def __init__(self, grid):
        rows, cols = len(grid), len(grid[0])
        self.count = 0
        self.root = [-1] * (rows*cols)
        self.rank = [0] * (rows*cols)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.root[i*cols + j] = i*cols + j
                    self.count += 1

    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution:
    def numsIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    continue
                for d in directions:
                    new_row, new_col = i + d[0], j + d[1]
                    # if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and grid[new_row][new_col] == '1':
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '1':
                        uf.union(i*cols + j, new_row*cols+new_col)

        return uf.count


if __name__ == "__main__":
    sol = Solution()
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    print(sol.numsIslands(grid))

