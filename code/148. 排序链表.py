"""
148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]
"""
""" 题解
归并排序。先通过快慢指针将原链表分为两前后两部分，然后新建一个链表对前后链表排序并返回。
4->2->1->3->None
     slow
4->2->None  1->3->None
4->None 2->None     1->None 3->None
2->4->None      1->3->None => 1->2->3->4->None
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        # 中点
        slow, fast = head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        new_head = ListNode(-1)
        p = new_head
        while left and right:
            if left.val <= right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next

        if left:
            p.next = left
        if right:
            p.next = right
        return new_head.next
