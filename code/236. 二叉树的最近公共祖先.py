"""
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”



示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
"""
""" 题解
DFS。递归终止条件当前根节点为p或q或None，l=dfs(root.left),r=dfs(root.right)，l&r时，当前root即为公共节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 终止条件，当前节点等于空或当前节点为p或q
        if not root:
            return None
        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        # 左右子树都没有p和q
        if not l and not r:
            return None
        # 左子树没有，右子树第一个为p或q的就是最近公共节点
        if not l:
            return r
        # 右子树没有，左子树第一个为p或q的就是最近公共节点
        if not r:
            return l
        # 左右子树有p和q
        return root
