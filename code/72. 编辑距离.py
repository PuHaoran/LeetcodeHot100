"""
72. 编辑距离
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""
""" 题解
①状态表示。f(i,j)为word1的第i个位置转化为word2的第j个位置的最少操作数。
②状态转移。f(i,j) = min(f(i,j-1), f(i-1,j), f[i-1][j-1]+1)+1
          f(i,j) = min(f[i][j], f[i-1][j-1]) w[i] == w[j]
a
ab  i=0 j=1 增加1
ab
a   i=1 j=0 去掉1
ab  
ac  i=1 j=1 更新1/0
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = list(word1)
        word2 = list(word2)
        n, m = len(word1), len(word2)
        f = [[0]*(m+1) for _ in range(n+1)]
        for i in range(m+1):
            f[0][i] = i
        for i in range(n+1):
            f[i][0] = i
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i][j-1], f[i-1][j], f[i-1][j-1])+1
        return f[n][m]


word1 = ""
word2 = "a"
solution = Solution()
print(solution.minDistance(word1, word2))