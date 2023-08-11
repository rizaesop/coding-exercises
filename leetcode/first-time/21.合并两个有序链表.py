#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        p = dummy
        p1 = l1
        p2 = l2

        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next

        if p1 is not None:
            p.next = p1

        if p2 is not None:
            p.next = p2

        return dummy.next


# @lc code=end

# 2023-08-11
# 题目没给listnode 定义，要自己写

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1: return l2  # 终止条件，直到两个链表都空
#         if not l2: return l1
#         if l1.val <= l2.val:  # 递归调用
#             l1.next = self.mergeTwoLists(l1.next,l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1,l2.next)
#             return l2
# 在看某大佬写的递归代码，差点头都吓掉了
