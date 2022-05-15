"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""
""" 题解
①BFS。while q.size():for i in range(len(q)): t = q.pop() 扩展q.appendleft/appendright。②递归
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        from collections import deque
        q = deque()
        res = 0
        q.append(root)
        while len(q):
            res += 1
            count = len(q)
            for _ in range(count):
                t = q.pop()
                if t.left:
                    q.appendleft(t.left)
                if t.right:
                    q.appendleft(t.right)
        return res


# 法二：递归。
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
