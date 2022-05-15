"""
494. 目标和
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。



示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1
"""
""" 题解
①状态表达。f(i,j)代表0-i个元素进行加减可以得到元素j的方法数量。
②状态转移。f(i,j)=f(i-1,j-nums[i]) + result(i-1,j+nums[i])

加法的总和x，减法(无符号)的总和sum-x，则x-(sum-x)=target，即x=(target+sum)//2，问题转化为装满容量为x的背包，有多少种方法。
eg:(5+3)//2=4。
f(i,j)代表0-i个元素加减可以得到元素j的个数。
f(i,j)=f(i-1, j-nums[i])
"""


class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        res = 0
        s = sum(nums)
        if (target+s) % 2 == 1:
            return 0
        if abs(target) > s:
            return 0



# class Solution:
#     def findTargetSumWays(self, nums, target: int) -> int:
#         global res, t
#         t, res = 0, 0
#
#         def dfs(u, t):
#             global res
#             if u == len(nums):
#                 if t == target:
#                     res += 1
#                 return
#             dfs(u+1, t+nums[u])
#             dfs(u+1, t-nums[u])
#         dfs(0, 0)
#         return res


nums = [1,1,1,1,1]
target = 3
solution = Solution()
print(solution.findTargetSumWays(nums, target))
