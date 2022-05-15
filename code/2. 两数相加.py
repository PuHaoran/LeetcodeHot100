"""
2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。



示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""
""" 题解
直接遍历，先遍历两链表，然后遍历剩余链表。建立一个头节点作为新建链表的起始节点（哨兵节点）。
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        p, q, l = l1, l2, head
        t, flag = 0, 0
        while p and q:
            t = p.val + q.val + flag
            flag = 0
            if t >= 10:
                flag = 1
                t -= 10
            l.next = ListNode(t)
            p, q, l = p.next, q.next, l.next
        while p:
            t = p.val + flag
            flag = 0
            if t >= 10:
                flag = 1
                t -= 10
            l.next = ListNode(t)
            p, l = p.next, l.next
        while q:
            t = q.val + flag
            flag = 0
            if t >= 10:
                flag = 1
                t -= 10
            l.next = ListNode(t)
            q, l = q.next, l.next
        if flag:
            l.next = ListNode(1)
        return head.next


""" 题解
递归解题。递归是当前两个节点和上一个进位相加作为新建节点的值。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def f(l1, l2, l, carry=0):
            if not l1 and not l2:
                if carry:
                    l.next = ListNode(carry)
                return
            t = carry
            if l1:
                t += l1.val
                l1 = l1.next
            if l2:
                t += l2.val
                l2 = l2.next
            carry = t // 10
            node = ListNode(t%10)
            l.next = node
            f(l1, l2, l.next, carry)
        l = ListNode(-1)
        f(l1, l2, l)
        return l.next
