"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
"""
""" 题解
双指针。先建立一个头节点，然后双指针判断较小的节点为下一个节点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        l = ListNode(-1)
        p = l
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        p.next = list1 if list1 else list2
        return l.next


"""
递归题解，node.next = f(node.next, other_node)，递归边界是某一条为None。
"""


class Solution:
    def mergeTwoLists(self, list1, list2):
        def get_list(list1, list2):
            if not list1:
                return list2
            elif not list2:
                return list1
            else:
                if list1.val < list2.val:
                    list1.next = get_list(list1.next, list2)
                    return list1
                else:
                    list2.next = get_list(list1, list2.next)
                    return list2
        return get_list(list1, list2)
