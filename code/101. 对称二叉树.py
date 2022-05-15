"""
101. 对称二叉树
给你一个二叉树的根节点 root ， 检查它是否轴对称。



示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
"""
""" 题解
法一：先对树进行翻转得到镜像树，然后递归判断原树和镜像树是否相等。
法二：判断左节点的左孩子与右节点的右孩子和左节点的右孩子和右节点的左孩子是否相等。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        import copy
        def dfs(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
            return root
        root2 = copy.deepcopy(root)
        dfs(root2)

        def is_same(root, root2):
            if not root and not root2:
                return True
            if not root or not root2:
                return False
            if root.val != root2.val:
                return False
            return is_same(root.left, root2.left) and is_same(root.right, root2.right)
        return is_same(root, root2)
