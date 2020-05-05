class TreeNode:
    def __init_(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self,root:TreeNode,p: TreeNode,q: TreeNode):
        """
        236. 二叉树的最近公共祖先
            给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

            百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
        """
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left:
            return right
        if not right:
            return left
        return root


    def lowestCommonAncestorOfBinarySearchTree(self,root:TreeNode,p:TreeNode,q:TreeNode):
        """
        最近公共祖先: 针对二叉搜索树，递归法
        """
        if root == None or root == p or root == q:
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root


    def lowestCommonAncestorOfBinarySearchTree(self,root:TreeNode,p:TreeNode,q:TreeNode):
        """
        最近公共祖先: 针对二叉搜索树，迭代法
        """
        if root == None or root == p or root == q:
            return root
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root