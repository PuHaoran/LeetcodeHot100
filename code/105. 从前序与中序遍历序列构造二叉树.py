"""
105. 从前序与中序遍历序列构造二叉树
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。



示例 1:


输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
"""
""" 题解
采用先序遍历构造二叉树，每次遍历缩小前序和中序区间。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def dfs(preorder, l, r):
            if l == r:
                return TreeNode(inorder[l])
            if l > r:
                return None
            t = preorder[0]
            idx = inorder.index(t)
            node = TreeNode(t)
            node.left = dfs(preorder[1:idx-l+1], l, idx-1)
            node.right = dfs(preorder[idx-l+1:], idx+1, r)
            return node

        res = dfs(preorder, 0, len(preorder)-1)
        return res
