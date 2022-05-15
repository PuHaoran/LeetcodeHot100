"""
739. 每日温度
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指在第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。



示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]
"""
""" 题解
维持单调递减队列，若当前队列不为空且当前温度大于等于栈顶温度则退栈，否则进栈。
"""


class Solution:
    def dailyTemperatures(self, temperatures):
        queue, p, q = [0] * 100010, -1, -1
        res = []
        for i in range(len(temperatures)-1, -1, -1):
            while p != q and temperatures[i] >= queue[q][0]:
                q -= 1
            if p != q:
                res.append(queue[q][1]-i)
            else:
                res.append(0)
            q += 1
            queue[q] = (temperatures[i], i)
        return res[::-1]


temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))
