"""
114. 二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。


示例 1：


输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
"""
""" 题解
先序遍历，保存节点到数组中，然后再遍历数组重构树。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        arr = []
        def dfs(root):
            if not root:
                return
            arr.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        pre = arr[0]
        for i in range(1, len(arr)):
            cur = arr[i]
            pre.left = None
            pre.right = cur
            pre = cur
