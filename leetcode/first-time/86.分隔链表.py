#
# @lc app=leetcode.cn id=86 lang=python
#
# [86] 分隔链表
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
class Solution(object):
    def partition(self, head, x):
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1, p2 = dummy1, dummy2
        p = head # !
        while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            temp = p.next
            p.next = None
            p = p.next
        p.next = dummy2.next
        return temp

# @lc code=end

