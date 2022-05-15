"""
234. 回文链表
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
示例 1：
输入：head = [1,2,2,1]
输出：true
示例 2：
输入：head = [1,2]
输出：false
"""
""" 题解
双指针+链表翻转。先通过快慢指针找到链表后半部分，然后对后半部分进行翻转，再进行比较。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p, q = head, head
        while q:
            p = p.next
            q = q.next
            if q:
                q = q.next
        l = None
        while p:
            p_next = p.next
            p.next = l
            l = p
            p = p_next
        p = head
        while l:
            if l.val != p.val:
                return False
            l = l.next
            p = p.next
        return True
