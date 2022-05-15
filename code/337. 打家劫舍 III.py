"""
337. 打家劫舍 III
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。
示例 1:
输入: root = [3,2,3,null,3,null,1]
输出: 7
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
"""
""" 题解
后续遍历+动态规划。
①状态表示。f(i,0)不选择i节点的最高金额，f(i,1)选择i节点的最高金额。
②状态转移。f(i,0)=max(f(i.left,0), f(i.left,1))+max(f(i.right,0),f(i.right,1))
          f(i,1)=f(i.left,0)+f(i.right,0)
          初始化边界d[None] = [0, 0]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        d = {}
        d[None] = [0, 0]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            d[root] = [0, 0]
            d[root][0] = max(d[root.left][0], d[root.left][1]) + max(d[root.right][0], d[root.right][1])
            d[root][1] = d[root.left][0]+d[root.right][0]+root.val
            return d[root]
        res = dfs(root)
        return max(res)
