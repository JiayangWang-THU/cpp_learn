#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
    #先把短的消耗完，所以这里用and
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
    #多余长度的直接接到后面就行
        while list1:
            cur.next = ListNode(list1.val)
            list1 = list1.next
            cur = cur.next

        while list2:
            cur.next = ListNode(list2.val)
            list2 = list2.next
            cur = cur.next

        return dummy.next

"""
这个就不用复制重新建节点了，直接把原有的节点指针接上就行
        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # 把剩下那一条直接接上
        cur.next = list1 if list1 else list2
        return dummy.next
"""
# @lc code=end

