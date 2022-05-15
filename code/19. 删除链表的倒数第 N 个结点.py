"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
"""
""" 题解
快慢双指针。快指针先走，当前后间隔>n时，慢指针再走。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = ListNode(-1)
        l.next = head
        p, q = l, l
        cnt = 0
        while q:
            if cnt > n:
                p = p.next
            q = q.next
            cnt += 1
        p.next = p.next.next
        return l.next
