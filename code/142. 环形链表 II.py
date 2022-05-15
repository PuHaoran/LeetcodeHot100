"""
142. 环形链表 II
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。
"""
""" 题解
                             b
          <-            -----
                    a  /     \
——————————————————————/       \
                     /---------\
                           x
双指针。快慢双指针，两指针相遇b点，此时2(a+b)=a+b+x+b=>x=a，然后让快指针从头开始遍历并保持和慢指针一样的速度，最终相遇于a点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow, fast = head.next, head.next.next
        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next

        return slow
