"""
96. 不同的二叉搜索树
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。



示例 1：


输入：n = 3
输出：5
示例 2：

输入：n = 1
输出：1
"""
""" 题解
f(i)是以i为根节点的二叉搜索树的个数，g(i)是i个节点的二叉树数量，则g(n)=f(1)+f(2)...f(n)，f(i)=g(i-1)*g(n-i)。
 None                               ------------- 1
 1                                  ------------- 1
 1          2                       ------------- 2
  \        /
   2      1
  1      1      2           3        3    ------------- 5
  \       \     /\         /         /        
   2       3   1  3       1         2
    \      /              \         /
     3     2               2       1
   0*2 1*1 2*0 => 2+1+2=5
"""


class Solution:
    def numTrees(self, n: int) -> int:
        f = [0] * (n+1)
        f[0], f[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                f[i] += f[j-1] * f[i-j]
        return f[n]


n = 3
solution = Solution()
print(solution.numTrees(n))
