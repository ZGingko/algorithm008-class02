# 学习笔记
## 知识点总结
### 第13课 字典树和并查集
1. 字典树 Trie，又称单词查找树或键树，典型应用是用于统计和排序大量字符串
   1. 基本性质
       * 节点本身不存完整单词
       * 从根节点到某一个节点，路径上经过的字符连接起来，为该节点对应的字符串
       * 每个节点的所有子节点路径代表的字符都不相同
   2. 节点可存储额外信息（如，统计频次等）
   3. Trie树的核心思想是空间换时间：可最大限度地减少无谓的字符串比较，查询效率比哈希表高
   4. 利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的
    ```python
    # Trie树的代码实现
    class Trie:
        def __init__(self):
            self.root = {}
            self.end_of_word = "#"
        
        def insert(self, word):
            node = self.root
            for ch in word:
                node = node.setdefault(ch, {})
            node[self.end_of_word] = self.end_of_word

        def search(self, word):
            node = self.root
            for char in word:
                if char not in node:
                    return False
                node = node[char]
            return self.end_of_word in node

        def startWith(self, prefix):
            node = self.root
            for char in prefix:
                if char not in node:
                    return False
                node = node[char]
            return True
    ```
    ```python
    # 单词搜索 II
    END_OF_WORD = "#" # 字典树中完整单词的结束标识
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        if not words:
            return []
        self.result = set()
        # 构建 Trie树
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
        for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = i + dx, j + dy
            if 0 <= x < self.rows and 0 <= y < self.cols and board[x][y] != "@" and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp
    ```
    ##### 单词搜索时间复杂度分析:

    > 设置 `board` 行为 `m` ，列为 `n`，单词个数为 `k`，单词平均长度为 `l`，最大长度为`L`。其中，`findWords` 的复杂度由两部分组成：  
        > 1. 构建字典树：需要两层循环遍历所有单词及各单词的每个字符，复杂度为 $O(k*l)$
        > 2. 两层循环遍历 `board`：
            >       1. 循环内只有一个if语句及对应的dfs函数，极端情况下每次都要进入if语句，或者每次都不需要进入if语句，复杂度介于 $O(m * n)$ 和 $O(m * n) * O(dfs)$ 之间
            >       2. dfs的目标是搜索由当前字母（前缀）开头的单词，其复杂度与单词的长度相关，由于可以从4个方向进行搜索，最差情况下第一次4个方向，之后3个方向都要进行搜索而不回溯，那么复杂度为 $O(4 * 3^{L-1})$ 。   
    
    > 构建字典树相比两层循环的复杂度量级要低，所以整体复杂度取决于两层循环的复杂度。  
    > 综上，单词搜索的时间复杂度在 $O(m * n)$ 和$O(m * n * 4 * 3^{L-1})$之间    
2. 并查集 Disjoint Set
   1. 适用场景
        * 组团、配对问题
        * Group or not
   2. 基本操作
      1. `makeSet(s)` : 建立一个新的并查集，其中包含s个单元素集合
      2. `unionSet(x, y)` : 把元素x和元素y所在的集合合并，要求x和y所在集合不相交，如果相交则不合并
      3. `find(x)` : 找到元素x所在集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只需将它们各自的代表进行比较即可
    ```python
    # 并查集代码模板
    class UnionFind:
        def __init__(self, n):
            self.count = n
            self.root = [i for i in range(n)]
            self.rank = [0] * (n)

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
    ```
    ```python
    class UnionFind:
        def __init__(self, n):
            self.root = [i for i in range(n)]

        def parent(self, p, i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i: # 路径压缩
                x = i; i = p[i]; p[x] = root
            return root
        
        def union(self, p, i, j):
            pi = self.parent(p, i)
            pj = self.parent(p, j)
            p[pi] = pj
    ```
### 第14课 高级搜索
1. 初级搜索
   1. 优化方式：不重复（Fibonacci）、剪枝（生成括号问题）
   2. 搜索方向：
      1. DFS: Depth First Search 深度优先搜索
      2. BFS: Breadth First Search 广度优先搜索
2. 高级搜索
   1. 剪枝
   2. 双向BFS
   3. 启发式搜索（A*） Heuristic Search
      1. 启发式函数：h(n)，用来评价哪些节点最有希望成为目标节点，h(n)会返回一个非负实数，也可认为是从节点n到目标节点路径的估价成本
      2. 启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测哪个邻居节点会导向一个目标   
   ```python
    # DFS 代码模板

    # 递归写法
    visited = set() 
    def dfs(node, visited):
        if node in visited: # terminator
            # already visited 
            return 

        visited.add(node) 
        # process current node here. 
        ...
        for next_node in node.children(): 
            if next_node not in visited: 
                dfs(next_node, visited)
    
    # 非递归写法
    def DFS(self, tree):
        if tree.root is None: 
            return [] 

        visited, stack = [], [tree.root]
        while stack: 
            node = stack.pop() 
            visited.add(node)

            process (node) 
            # 生成相关的节点
            nodes = generate_related_nodes(node) 
            stack.push(nodes) 

        # other processing work 
        ...
   ```
   ```python
    # BFS 代码模板
    def BFS(graph, start, end):
        visited = set()
        queue = [] 
        queue.append([start]) 

        while queue: 
            node = queue.pop() 
            visited.add(node)

            process(node) 
            nodes = generate_related_nodes(node) 
            queue.push(nodes)

        # other processing work 
        ...
   ```
   ```python
   # A* search
   def AstarSearch(graph, start, end):
       pq = collections.priority_queue() # 优先级 -> 估价
       pq.append([start])
       visited.add(start)

       while pq:
           node = pq.pop()
           visited.add(node)

           process(node)
           nodes = generate_related_nodes(node)
           unvisited = [node for node in nodes if node not in visited]
           pq.push(unvisited)
   ```
### 第15课 红黑树和AVL树
1. AVL树
    1、平衡二叉搜索树
    2、每个节点存 Balance Factor = {-1, 0, 1}
    3、四种旋转操作（左旋，右旋，左右旋，右左旋）  
   不足：节点需要存储额外信息，且调整次数频繁
2. 红黑树：红黑树是一种近似平衡的二叉搜索树，它能够确保任何一个节点的左右子树的高度差小于两倍。
    1、每个节点要么是红色要么是黑色
    2、根节点是黑色
    3、每个叶节点（NIL节点，空节点）是黑色的
    4、不能有相邻接的两个红色节点
    5、从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点。
3. AVL和红黑树比较
    1、查找：AVL比红黑树快
    2、插入和删除：红黑树比AVL快
    3、内存：AVL比红黑树要占用大