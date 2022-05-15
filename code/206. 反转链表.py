"""
206. 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]
"""
""" 题解
一边遍历链表，一边将当前节点作为头结点，链接之前翻转后的链表。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        q = None
        p = head
        while p:
            p_next = p.next
            p.next = q
            q = p
            p = p_next
        return q
