"""
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。


示例 1:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""
""" 题解
单调栈。一个栈存储原数据，另一个栈存储单调递减数据。
"""


class MinStack:

    def __init__(self):
        self.t = -1
        self.t2 = -1
        self.s = [0] * 30010
        self.s2 = [0] * 30010

    def push(self, val: int) -> None:
        self.t += 1
        self.s[self.t] = val
        if self.t2 == -1 or val <= self.s2[self.t2]:
            self.t2 += 1
            self.s2[self.t2] = val

    def pop(self) -> None:
        if self.t == -1:
            return None
        top_val = self.s[self.t]
        self.t -= 1
        if top_val == self.s2[self.t2]:
            self.t2 -= 1

    def top(self) -> int:
        if self.t == -1:
            return None
        return self.s[self.t]

    def getMin(self) -> int:
        if self.t2 == -1:
            return None
        return self.s2[self.t2]
