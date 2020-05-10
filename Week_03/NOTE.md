# 学习笔记
## 知识点总结
### 第7课 泛型递归、树的递归
1. 递归 Recursion
   1. 递归本质上也是一种循环：通过函数体来进行的循环
   2. 从前有座山，山上有座庙，庙里有个老和尚，和尚正在讲故事：从前有座山……
   3. 盗梦空间：向下进入不同梦境；向上又回到原来一层
2. 递归代码模板
   ```python
   def recursion(level,param1,param2,...):
       # recursion terminator
       if level > MAX_LEVEL:
           process_result
           return
        
        # process logic in current level
        process(level, data...)

        #drill down
        self.recursion(level+1,param1,param2,...)

        # reverse the currcent level status if needed
   ```
   ```java
   public void recur(int level,int param){
       //terminator 
       if(level>MAX_LEVEL)  {
           //process result
           return;
       }

       //process current logic
       process(level, param);

       //drill down
       recur(level:level+1,newParam);

       //reverse current status
   }
   ```
3. 思维要点
   1. 不要人肉进行递归（最大误区）
   2. 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
   3. 数学归纳法思维
4. 树的面试题解法一般都是递归：
   1. 节点的定义
   2. 重复性（自相似性）
   3. 二叉树的遍历代码模板
   ```python
   # 前序遍历
   def preorder(self,root):
       if root:
           self.traverse_path.append(root.val)
           self.preorder(root.left)
           self.preorder(root.right)
    
    # 中序遍历
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    # 后序遍历
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)
   ```
### 第8课 分治、回溯
1. 分治 Divide & Conquer
   1. 本质上是一种递归：特殊的递归
   2. 重复性
      1. 最优重复性 -> 动态规划
      2. 最近重复性 -> 根据构造和特性，使用分治或回溯等方法
   3. 找重复性，分解成若干子问题，最后组合各子问题的结果
   4. 分治代码模板
   ```python
    def divide_conquer(problem, param1, param2,...):
        # recursion terminator
        if problem is None:
            print_result
            return

        # prepare data
        data = prepare_data(problem)
        subproblems = split_problem(problem, data)

        # conquer subproblems
        subresult1 = self.divide_conquer(subproblems[0], p1,...)
        subresult2 = self.divide_conquer(subproblems[1], p1,...)
        subresult3 = self.divide_conquer(subproblems[2], p1,...)
        ...

        # process and generate the final result
        result = process_result(subresult1, subresult2, subresult3,...)

        # revert the current level states
   ```
2. 回溯 Backtracking
   1. 采用试错的思想，尝试分步去解决一个问题。当发现有的分步不能得到有效的正确解答，则取消前一步甚至是几步的计算，再通过其他可能的分步解答再次尝试寻找问题的答案
   2. 回溯法通常用最简单的递归方法实现，反复重复上述的步骤后可能出现的两种情况
      1. 找到一个可能存在的正确的答案
      2. 在尝试了所有可能的分步方法后宣告问题没有答案
   3. 在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算


回溯问题的算法框架
```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

    
    for 选择 in 选择列表:
        # 做选择
        将该选择从选择列表移除
        路径.add(选择)
        backtrack(路径, 选择列表)
        # 撤销选择
        路径.remove(选择)
        将该选择再加入选择列表
```
全排列代码框架
```java
/* 主函数，输入一组不重复的数字，返回它们的全排列 */
List<List<Integer>> permute(int[] nums) {
    // 记录「路径」
    LinkedList<Integer> track = new LinkedList<>();
    backtrack(nums, track);
    return res;
}

// 路径：记录在 track 中
// 选择列表：nums 中不存在于 track 的那些元素
// 结束条件：nums 中的元素全都在 track 中出现
void backtrack(int[] nums, LinkedList<Integer> track) {
    // 触发结束条件
    if (track.size() == nums.length) {
        res.add(new LinkedList(track));
        return;
    }
    
    for (int i = 0; i < nums.length; i++) {
        // 排除不合法的选择
        if (track.contains(nums[i]))
            continue;
        // 做选择
        track.add(nums[i]);
        // 进入下一层决策树
        backtrack(nums, track);
        // 取消选择
        track.removeLast();
    }
}
```
N皇后问题
```c++
vector<vector<string>> res;

/* 输入棋盘边长 n，返回所有合法的放置 */
vector<vector<string>> solveNQueens(int n) {
    // '.' 表示空，'Q' 表示皇后，初始化空棋盘。
    vector<string> board(n, string(n, '.'));
    backtrack(board, 0);
    return res;
}

// 路径：board 中小于 row 的那些行都已经成功放置了皇后
// 选择列表：第 row 行的所有列都是放置皇后的选择
// 结束条件：row 超过 board 的最后一行
void backtrack(vector<string>& board, int row) {
    // 触发结束条件
    if (row == board.size()) {
        res.push_back(board);
        return;
    }
    
    int n = board[row].size();
    for (int col = 0; col < n; col++) {
        // 排除不合法选择
        if (!isValid(board, row, col)) 
            continue;
        // 做选择
        board[row][col] = 'Q';
        // 进入下一行决策
        backtrack(board, row + 1);
        // 撤销选择
        board[row][col] = '.';
    }
}

/* 是否可以在 board[row][col] 放置皇后？ */
bool isValid(vector<string>& board, int row, int col) {
    int n = board.size();
    // 检查列是否有皇后互相冲突
    for (int i = 0; i < n; i++) {
        if (board[i][col] == 'Q')
            return false;
    }
    // 检查右上方是否有皇后互相冲突
    for (int i = row - 1, j = col + 1; 
            i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 'Q')
            return false;
    }
    // 检查左上方是否有皇后互相冲突
    for (int i = row - 1, j = col - 1;
            i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 'Q')
            return false;
    }
    return true;
}

// 函数找到一个答案后就返回 true
bool backtrack(vector<string>& board, int row) {
    // 触发结束条件
    if (row == board.size()) {
        res.push_back(board);
        return true;
    }
    ...
    for (int col = 0; col < n; col++) {
        ...
        board[row][col] = 'Q';

        if (backtrack(board, row + 1))
            return true;
        
        board[row][col] = '.';
    }

    return false;
}
```
C++ 解法
```c++
class Solution {
public:
    std::vector<std::vector<std::string> > solveNQueens(int n) {
        std::vector<std::vector<std::string> > res;
        std::vector<std::string> nQueens(n, std::string(n, '.'));
        solveNQueens(res, nQueens, 0, n);
        return res;
    }
private:
    void solveNQueens(std::vector<std::vector<std::string> > &res, std::vector<std::string> &nQueens, int row, int &n) {
        if (row == n) {
            res.push_back(nQueens);
            return;
        }
        for (int col = 0; col != n; ++col)
            if (isValid(nQueens, row, col, n)) {
                nQueens[row][col] = 'Q';
                solveNQueens(res, nQueens, row + 1, n);
                nQueens[row][col] = '.';
            }
    }
    bool isValid(std::vector<std::string> &nQueens, int row, int col, int &n) {
        //check if the column had a queen before.
        for (int i = 0; i != row; ++i)
            if (nQueens[i][col] == 'Q')
                return false;
        //check if the 45° diagonal had a queen before.
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; --i, --j)
            if (nQueens[i][j] == 'Q')
                return false;
        //check if the 135° diagonal had a queen before.
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; --i, ++j)
            if (nQueens[i][j] == 'Q')
                return false;
        return true;
    }
};
```
N皇后问题 解法，Java版本，带注释
```java
class Solution {
    private List<List<String>> output = new ArrayList<>();

    // 用于标记是否被列方向的皇后攻击
    int[] rows;
    // 用于标记是否被主对角线方向的皇后攻击
    int[] mains;
    // 用于标记是否被次对角线方向的皇后攻击
    int[] secondary;
    // 用于存储皇后放置的位置
    int[] queens;

    int n;

    public List<List<String>> solveNQueens(int n) {
        // 初始化
        rows = new int[n];
        mains = new int[2 * n - 1];
        secondary = new int[2 * n - 1];
        queens = new int[n];
        this.n = n;

        // 从第一行开始回溯求解 N 皇后
        backtrack(0);

        return output;    
    }

    // 在一行中放置一个皇后
    private void backtrack(int row) {
        if (row >= n) return;
        // 分别尝试在 row 行的每一列中放置皇后
        for (int col = 0; col < n; col++) {
            // 判断当前放置的皇后不被其他皇后的攻击
            if (isNotUnderAttack(row, col)) {
                // 选择，在当前的位置上放置皇后
                placeQueen(row, col);
                // 当当前行是最后一行，则找到了一个解决方案
                if (row == n - 1) addSolution();
                // 在下一行中放置皇后
                backtrack(row + 1);
                // 撤销，回溯，即将当前位置的皇后去掉
                removeQueen(row, col);
            }
        }
    }

    // 判断 row 行，col 列这个位置有没有被其他方向的皇后攻击
    private boolean isNotUnderAttack(int row, int col) {
        // 判断的逻辑是：
        //      1. 当前位置的这一列方向没有皇后攻击
        //      2. 当前位置的主对角线方向没有皇后攻击
        //      3. 当前位置的次对角线方向没有皇后攻击
        int res = rows[col] + mains[row - col + n - 1] + secondary[row + col];
        // 如果三个方向都没有攻击的话，则 res = 0，即当前位置不被任何的皇后攻击
        return res == 0;
    }

    // 在指定的位置上放置皇后
    private void placeQueen(int row, int col) {
        // 在 row 行，col 列 放置皇后
        queens[row] = col;
        // 当前位置的列方向已经有皇后了
        rows[col] = 1;
        // 当前位置的主对角线方向已经有皇后了
        mains[row - col + n - 1] = 1;
        // 当前位置的次对角线方向已经有皇后了
        secondary[row + col] = 1;
    }

    // 移除指定位置上的皇后
    private void removeQueen(int row, int col) {
        // 移除 row 行上的皇后
        queens[row] = 0;
        // 当前位置的列方向没有皇后了
        rows[col] = 0;
        // 当前位置的主对角线方向没有皇后了
        mains[row - col + n - 1] = 0;
        // 当前位置的次对角线方向没有皇后了
        secondary[row + col] = 0;
    }

    /**
     * 将满足条件的皇后位置放入output中
     */
    public void addSolution() {
        List<String> solution = new ArrayList<String>();
        for (int i = 0; i < n; ++i) {
            int col = queens[i];
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < col; ++j) sb.append(".");
            sb.append("Q");
            for(int j = 0; j < n - col - 1; ++j) sb.append(".");
            solution.add(sb.toString());
        }
        output.add(solution);
    }
}
```