# 学习笔记
## 知识点总结
### 第9课 深度优先搜索与广度优先搜索
1. 遍历搜索：在树（图/状态集）中寻找特定的节点
   1. 每个节点都要访问一次
   2. 每个节点仅访问一次
   3. 对于节点访问顺序不限
        * 深度优先：Depth First Search
        * 广度优先：Breadth First Search
2. 深度优先搜索 DFS
   ```python
    # 二叉树的深度优先搜索代码模板
    def DFS(node):
        if node in visited:
            # already visited
            return
        visited.add(node)

        # process current node
        # ... # logic here

        dfs(node.left)
        dfs(node.right)
    ```
    ```python
    # N叉树深度优先代码模板
    visited = set()
    def DFS(node, visited):
        if node in visited:
            # already visited 
            return

        visited.add(node)
        # process current node here
        ...

        for next_node in node.children:
            if not next_node in visited:
                dfs(next_node, visited)
    ```
    ```python
    # DFS - 非递归写法
    def DFS(tree):
        if tree.root is None:
            return []
        visited, stack = [], [tree.root]

        while stack:
            node = stack.pop()
            visited.add(node)

            process(node)
            nodes = generate_related_nodes(node)
            stack.push(nodes)

        # other processing work
        ...
    ```
3. 广度优先搜索 BFS
   ```python
    def BFS(graph, start, end):
        queue = []
        queue.append([start])
        visited.add(start)

        while queue: 
            node = queue.pop()
            visited.add(node)

            process(node)
            nodes = generate_relater_nodes(node)
            queue.push(nodes)
        # other processing work
        ...
   ```
   
### 第10课 贪心算法
1. 贪心算法 Greedy
   * 贪心算法是一种在每一步选择中采取当前状态最优或最好的选择，从而希望导致结果是全局最优
   * 贪心算法与动态规划的不同
        1. 贪心算法会对每个子问题的解决方案都做出选择，并且不能回退
        2. 动态规划则会保存之前的运算结果，并根据以前的结果在当前进行选择，可以回退
            > 贪心：当下做局部最优判断

            > 回溯：能够回退

            > 动态规划：最优判断 + 回退
2. 贪心算法主要解决一些最优化问题，如：求图的最小生成树、求哈夫曼编码。实际生活和工程中的问题，贪心法一般不能得到我们想要的答案
3. 一旦一个问题可以通过贪心法解决，那么贪心法一般就是解决该问题的最好办法。
4. 适用场景：问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构

### 第11课 二分查找
1. 能进行二分查找的前提
   1. 目标函数单调性（单调递增或递减）
   2. 存在上下界（bounded）
   3. 能够通过索引访问（index accessible）
2. 代码模板
   ```python
    # 二分查找
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target: # 找到目标值，返回结果
            break or return result
        elif array[mid] < target: # 目标值在右侧，左边界右移
            left = mid + 1
        else: # 否则，目标值在左侧，右边界左移
            right = mid -1

   ```
### 思考题：
> 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

#### 解题思路：该问题等同于求半有序数组中的最小值，中间无序的地方即为最小值所在位置
1. 取得中间位置 `nums[mid] `的值
2. `if nums[mid] > nums[0] `则 `[0, mid] `为有序区间，所找位置在 `[mid+1, n] `
   1. `if nums[mid] > nums[mid+1] `，则 `mid + 1 `即为所找的位置
   2. 否则 `nums = nums[mid+1,n] `，回到第1步
3. `if nums[mid] < nums[0] `，则所找位置在 `[0, mid] `
   1. `if nums[mid] < nums[mid-1] `，则 `mid - 1 `即为所找的位置，返回
   2. 否则 ` nums = nums[:mid] `，回到第1步
    ```python
    def findMin(self,nums:List[int]):
        if len(nums) == 1:
            return nums[0]
        left,right = 0, len(nums) - 1

        if nums[right] > nums[0]: # 如果数组没有发生旋转，则第一个元素就是最小元素
            return nums[0]
            
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
                
            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[0]: 
                left = mid + 1 # 发生旋转的数组[0,mid]有序，则最小值肯定右侧区间中
            else:
                right = mid - 1
    ```

### 不同情况的二分查找代码框架整理
1. 二分查找基本框架
    ```java
    int binarySearch(int[] nums, int target){
        int left = 0, right = ...;

        while(...){
            int mid = (left + right) / 2;
            if(nums[mid] == target){
                ...
            }else if(nums[mid] < target){
                ...
            }else if(nums[mid] > target){
                ...
            }
        }
        return ...;
    }
    ```
2. 基本的二分搜索
    ```java
    int binarySearch(int[] nums, int target){
        int left = 0;
        int right = nums.length - 1;

        while(left <= right){
            int mid = (left + right) / 2;
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] < target){
                left = mid + 1;
            }else if(nums[mid] > target){
                right = mid - 1;
            }
        }
        return -1;
    }
    ```
3. 寻找左边界的二分搜索
    ```java
    int left_bound(int[] nums, target){
        if (nums.length == 0) return -1;
        int left = 0;
        int right = nums.length;

        while(left < right){
            int mid = (left + right) / 2;
            if(nums[mid] == target){
                right = mid;
            }else if(nums[mid] < target){
                left = mid + 1;
            }else if(nums[mid] > target){
                right = mid;
            }
        }
        // target 比所有数都大
        if (left == nums.length) return -1;
        // 类似之前算法的处理方式
        return nums[left] == target ? left : -1;
    }
    ```
4. 寻找右边界的二分查找
    ```java
    int right_bound(int[] nums, int target){
        if (nums.length == 0) return -1;
        int left = 0;
        int right = nums.length;

        while(left < right){
            int mid = (left + right) / 2;
            if(nums[mid] == target){
                left = mid + 1;
            }else if(nums[mid] < target){
                left = mid + 1;
            }else if (nums[mid] > target){
                right = mid;
            }
        }
        if (left == 0) return -1;
        return nums[left-1] == target ? (left-1) : -1;
    }
    ```