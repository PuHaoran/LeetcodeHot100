"""
338. 比特位计数
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

输入：n = 5
输出：[0,1,1,2,1,2]
解释：
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""


class Solution:
    def countBits(self, n: int):
        def get_lowbit(m):
            cnt = 0
            while m:
                m = m&(m-1)
                cnt += 1
            return cnt
        res = []
        for i in range(n+1):
            res.append(get_lowbit(i))
        return res
