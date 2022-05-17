"""
23. 合并K个升序链表
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。



示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
"""
""" 题解
根据当前所有链表中最小的值建立新链表节点并将当前链表向前进一，一直到所有链表均指向None为止。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        head = ListNode(-1)
        p = head
        while 1:
            flag = 0
            idx_min = None
            value_min = 10010
            for i in range(len(lists)):
                if not lists[i]:
                    flag += 1
                else:
                    if lists[i].val < value_min:
                        idx_min = i
                        value_min = lists[i].val
            if flag == len(lists):
                break
            l = lists[idx_min]
            p.next = l
            p = p.next
            l = l.next
            lists[idx_min] = l
        return head.next
