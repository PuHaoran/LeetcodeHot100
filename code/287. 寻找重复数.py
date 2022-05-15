"""
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。



示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
"""
""" 题解
遍历数组，当前元素对应idx加负号，若当前元素对应idx已经为负号，则说明重复。
1 3 4 2 2 
0->1
1->3
2->4
3->2
4->2
0->1->3->2->4               b
          <-            -----
                   a   /     \
——————————————————————/       \
                     /---------\
                           x
b点为快慢指针相遇的点，a为环入口，则快指针相比慢指针多走了x+b，x+b也是慢指针走过的路径a+b，故x=a。
即快指针从头开始走a，刚好等于慢指针从b点开始走的x。
快指针：a+b+x+b = 2(a+b) => x = a                           
"""


class Solution:
    def findDuplicate(self, nums) -> int:
        slow, fast = nums[0], nums[nums[0]]
        #print(slow, fast)
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow

# class Solution:
#     def findDuplicate(self, nums) -> int:
#         for i in range(len(nums)):
#             if nums[abs(nums[i])-1] < 0:
#                 return abs(nums[i])
#             nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]


nums = [1,3,4,2,2]
solution = Solution()
print(solution.findDuplicate(nums))
