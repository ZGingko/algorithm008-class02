# 学习笔记
## 知识点总结
### 第12课 动态规划
1. 回顾 递归（Recursion）和分治（Divide & Conquer）：
   ```python
   # 递归代码模板
    def recursion(level, param):
        # recursion terminator
        if level > MAX_LEVEL:
            process result
            return
        
        # process logic in current level
        process(level, param)

        # drill down
        recursion(level+1, newParam)

        # reverse the current level status if needed
   ```
   ```python
    # 分治代码模板
    def divide_conquer(problem, param1, param2, ...):
        # terminator
        if problem is None:
            print result
            return
        
        # prepare data
        data = prepare_data(problem)
        subproblems = split_problem(problem, data)

        # conquer subproblems
        subresult1 = divide_conquer(subproblems[0], p1, ...)
        subresult2 = divide_conquer(subproblems[1], p1, ...)
        subresult3 = divide_conquer(subproblems[2], p1, ...)
        ...

        # process and generate the final result
        result = process_result(subresult1, subresult2, subresult3, ...)

        # revert the current level states
   ```
2. 动态规划 Dynamic Programing：动态递推
   * 将复杂的问题分解为简单的子问题（用一种递归的方式）
   * 动态规划 和 递归（Recursion）或者分治（Divide）没有本质上的区别（关键看有无最优子结构）
   * 共性：找重复子问题
   * 差异性：最优子结构，中途可以(必须)淘汰次优解
3. 解题思路
   1. 暴力求解，查看是否存在重复子问题
   2. DP：
        * 分治（找到重复子问题）
        * 状态数组定义
        * 确定DP方程
#### 通常DP有如下解法：
1. Top-Bottom 分治、记忆化，如利用数组存储中间结果
    ```python
    def fib(n, memo):
        if n <= 1:
            return n
        if memo[n] == 0:
            memo[n] = fib(n-1,memo) + fib(n-2, memo)
        return memo[n]        
    ```
2. Bottom-Up 设置初始值，循环递推
   
    a. 一维递推
    ```python
    a[0], a[1] = 0, 1
    for i in range(2, n):
        a[i] = a[i-1] + a[i-2]
    ```
    b. 多维递推，取舍最优子结构
    ```python
    def uniquePaths(m, n):
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
    ```
    c. 空间优化，滚动数组（二维 -> 一维）
    ```python
    def uniquePathsWithObstacles(obstacleGrid:List[List[int]]):
        width = len(obstacleGrid[0])
        dp = [None] * width
        dp[0] = 1
        for row in obstacleGrid:
            for i in range(width):
                if row[i] == 1:
                    dp[i] = 0
                elif i > 0:
                    dp[i] += dp[i-1]
        
        return dp[width-1]
    ```
    **关键点**

    1. 最优子结构：`opt[n] = best_of(opt[n-1], opt[n-2], ...)`
    2. 定义、存储中间状态：`opt[i]` (关键步骤)
    3. 递推公式（状态转移方程）
        * Fib: `opt[n] = opt[n-1] + opt[n-2]`
        * 二维路径: `opt[i][j] = opt[i+1][j] + opt[i][j+1]`，根据情况判断能否到达

### 实战例题

1. [爬楼梯问题](https://leetcode-cn.com/problems/climbing-stairs/description/)：

    * 重复性：当前楼梯只能从后面1阶或者后面2阶到达
    * 状态定义：同斐波那契数
    * DP方程：`F(n) = F(n-1) + F(n-2)`
    * 优化：由DP方程可知，当前楼梯只和后面1阶和2阶相关，因此只需要额外用两个变量保存即可,不需要保存整个数组
    * 拓展：相邻两步的步伐不能相同

2. [三角形最小路径和](https://leetcode-cn.com/problems/triangle/description/)：

    * 重复性：`problem(i, j) = min(sub(i+1, j), sub(i+1, j+1)) + a[i][j]`
    * 状态定义：`f[i][j]` 为走到最后一行的最小路径和
    * DP方程：`f(i, j) = min(f(i+1, j), f(i+1, j+1)) + a[i][j]`
    * 优化：在遍历数组时可知，当前行的状态只和下一行的状态有关，且计算完当前行后下一行的数据不会再被用到，可以考虑复用一维数组。由于需要覆盖前一行的状态，需要考虑是否会影响后面的计算，举例如下：

    ```
    [
           [2],
          [3,4],
         [6,5,7],
        [4,1,8,3]
    ]
    ```
    初始状态为最后一行，需要计算倒数第二行的状态，6处的状态为 `min(4, 1) + 6 = 7`，保存在 `4` 处（当前元素下标为 `0`），之后的计算不再使用 `4`（因为上面的元素只能往左下或者往右下一格），可以被安全覆盖，以此类推。因此只需要开一维数组，大小为最后一行（需要的长度最大），且将最后一行的值赋给一维数组作为初始状态。

3. [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)：

    * 重复性：如果选第 `i` 个元素，则最大子序列 `max_sum(i) = max(max_sum(i-1), 0) + a[i]`，即包含/不包含前一个数的子序和中较大值加上自己
    * 状态定义：`f[i]`表示从 `0` 到 `i` 个元素且包括i的累加和
    * DP方程：`f[i] = max(f(i-1), 0) + a[i]`，遍历数组，如果累加和为负数则丢弃累加和
    * 优化：由DP方程可知，`f(i)` 只和 `f(i-1)` 相关，只需要变量保存前一个最大子序和而不需要一维数组

4. [零钱兑换](https://leetcode-cn.com/problems/coin-change/)：

    * 重复性：类似爬楼梯，假设要凑齐 `11` 的面值，有 `1、2、5` 可选，则 `problem(11) = sub(11-1) + sub(11-2) + sub(11-5)` ，暴力求解找硬币数量最小就是递归层次最小，可以做BFS
    * 状态定义：`f(i)` 为凑到面值为 `i` 所需要的最小硬币数
    * DP方程：`f(n) = min(f(n-k), for k in [1, 2, 5]) + 1，k` 为可选面值
  
5. [打家劫舍](https://leetcode-cn.com/problems/house-robber/)：

    * 重复性：由于不能偷连续的房屋，因此偷到第 `i` 号房子的最高金额与第 `i-1`、`i-2` 号有关
    * 状态定义：`a[i]`表示从 `0...i` 号，且第 `i` 号必偷的最大值
    * DP方程：`f(n) = max(f(n-1), f(n-2) + a[n])`
    * 优化：类似爬楼梯，只需要变量保存前两个最大值，而不需要一维数组

6. [最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)：

    * 重复性：`i` 行 `j` 列只能从 `i-1` 行 `j` 列或 `i` 行 `j-1` 列走到，即从上面或者左边走到
    * 状态定义：`f(i,j)` 表示走到 `i` 行 `j` 列的最小路径和
    * DP方程：`f(i,j) = min(f(i-1, j), f(i, j-1)) + grid[i][j]`
    * 优化：类似三角形最小路径和，只需要一维数组保存状态。需要注意，由于i和j是从1开始枚举的，当i为0时需要额外计算