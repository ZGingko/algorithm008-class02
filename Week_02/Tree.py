class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class BinaryTreeNode(object):
    def __init__(self, val=None, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorder(self, root: Node):
        """
        589. N叉树的前序遍历 循环法
            给定一个 N 叉树，返回其节点值的前序遍历。
        """
        if not root:
            return []
        result,root = [],root and [root]
        while root:
            node = root.pop()
            result.append(node.val)
            if node.children: # 2020-04-22 晚加，前一晚还没问题？
                root += [child for child in node.children[::-1] if child]
        return result


    def preorder1(self, root: Node):
        if not root:
            return []
        result,root = [],root and [root]
        while root:
            node = root.pop()
            result.append(node.val)
            if node.children: # 2020-04-22 晚加，前一晚还没问题？
                root.extend(node.children[::-1])
        return result

    
    def preorder2(self, root: Node):
        """
        N叉树的前序遍历 递归法
        """
        if not root:
            return []
        result = []
        result.append(root.val)
        if root.children: # 2020-04-22 晚加，前一晚还没问题？
            for node in root.children: 
                result += self.preorder2(node)
        return result

    def postorder(self, root: Node):
        """N叉树的后序遍历 迭代法：先前序遍历，再反转结果"""
        if not root:
            return []        
        stack, result = [root, ], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.children:
                for child in node.children:
                    stack.append(child)                
        return result[::-1]

    
    def postorder1(self, root: Node):
        """N叉树的后序遍历 递归法"""
        if not root:
            return []        
        result = []
        if root.children:
            for node in root.children:
                result.extend(self.postorder1(node))
        result.append(root.val)   
        return result


    def levelOrder(self, root:Node):
        """N叉树的层序遍历"""
        if not root:
            return []
        result = []
        temp = [root]
        while temp:
            node = temp.pop(0)
            tmp = []
            if node.children:
                for item in node.children:
                    tmp.append(item.val)
                    temp.extend([item])
                result.append(tmp)
        return result


    def levelOrder1(self, root:Node):
        """N叉树的层序遍历,BFS"""
        if not root:
            return []
        result = []
        temp = [root]
        while temp:
            tmp = []
            for _ in range(len(temp)):
                item = temp.pop(0)
                tmp.append(item.val)
                if item.children:
                    temp.extend(item.children)
            result.append(tmp)
        return result

    
    def levelOrder2(self, root: 'Node'):
        """N叉树的层序遍历"""
        import collections
        if root is None:
            return []
        result = []
        queue = collections.deque([root])
        # queue.append(root)
        # visited = set(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(level)
        return result

    def levelOrderBinaryTree(self, root: BinaryTreeNode):
        """二叉树的层序遍历"""
        import collections
        if root is None:
            return []
        result = []
        queue = collections.deque([root])
        while queue:
            current_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result

    def levelOrderBinaryTree2(self, root: BinaryTreeNode):
        """二叉树的层序遍历"""
        if not root:return [] 
        self.result = []
        self._dfs(root,0)
        return self.result

    def _dfs(self,node,level):
        if not node :return
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(node.val)
        self._dfs(node.left,level+1)
        self._dfs(node.right,level+1)
    
    def preorderBinaryTree(self, root: BinaryTreeNode):
        """
        二叉树的前序遍历。迭代法
        """
        if not root:
            return []
        result,root = [],root and [root]
        while root:
            node = root.pop()
            result.append(node.val)
            if node.right:
                root.extend([node.right])
            if node.left:
                root.extend([node.left])
        return result


    def preorderBinaryTree2(self, root: BinaryTreeNode):
        """
        二叉树的前序遍历。递归法
        """
        if not root:
            return []
        result = [root.val]
        result.extend(self.preorderBinaryTree2(root.left))
        result.extend(self.preorderBinaryTree2(root.right))
        return result

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        二叉树的中序遍历 递归法
        """
        if not root:
            return []
        result = []
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result
    
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        二叉树的中序遍历 迭代法
        0、根节点入栈
        1、循环遍历左节点依次入栈直到叶子节点，cur指针指向栈顶节点
        2、栈顶节点出栈，并记录节点value值，cur指向栈顶节点的右节点，重复第1步
        3、输出最终的结果
        """
        if not root:
            return []
        result = []
        tmp = []
        cur = root
        while cur or len(tmp)>0:
            while cur:
                tmp.append(cur)
                cur = cur.left
            cur = tmp.pop()
            result.append(cur.val)
            cur = cur.right
        return result

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        二叉树的后序遍历 递归法
        """
        if not root:
            return []
        result = []
        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        二叉树的后序遍历 迭代法
        """
        if not root:
            return []        
        stack, result = [root, ], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.extend([node.left])
            if node.right:
                stack.extend([node.right])         
        return result[::-1]

    def postorderTraversal(self, root):
        """
        flag标记已访问的节点
        """
        result, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    result.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return result

    def lowestCommonAncestor(self,root,p,q):
        """
        最近公共祖先
        """
        if root==None or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left == None:
            return right
        if right == None:
            return left
        return root

    def lowestCommonAncestor2(self,root,p,q):
        """最近公共祖先: 针对二叉搜索树"""
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root

    def lowestCommonAncestor22(self,root,p,q):
        """最近公共祖先: 针对二叉搜索树"""
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
    
    def lowestCommonAncestor222(self,root,p,q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

    def maxDepth(self,root:BinaryTreeNode):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

    def minDepth(self,root:BinaryTreeNode):
        if not root :return 0
        if not root.left:
            return self.minDepth(root.right)+1
        if not root.right:
            return self.minDepth(root.left)+1
        
        leftMinDepth = self.minDepth(root.left)
        rightMinDepth =self.minDepth(root.right)

        return 1 + min(leftMinDepth,rightMinDepth)


if __name__ == "__main__":
    solution = Solution()
    root = Node(1)
    root.children = [Node(3),Node(2),Node(4)]
    root.children[0].children = [Node(5),Node(6)]
    root.children[1].children = [Node(7),Node(8)]

    print(solution.levelOrder1(root))
    print(solution.postorder1(root))


    # # Driver code to test above 
    # arr = [ 12, 11, 13, 5, 6, 7] 
    # solution.heapSort(arr) 
    # n = len(arr) 
    # print ("Sorted array is") 
    # for i in range(n): 
    #     print ("%d" % arr[i]), 
    # # This code is contributed by Mohit Kumra 