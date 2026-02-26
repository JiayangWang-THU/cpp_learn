#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        ge_dummy = ListNode(0)
        less = less_dummy
        ge = ge_dummy

        cur = head
        while cur:
            nxt = cur.next
            cur.next = None  # 断开，避免形成环
            if cur.val < x:
                less.next = cur
                less = cur
            else:
                ge.next = cur
                ge = cur
            cur = nxt

        less.next = ge_dummy.next
        return less_dummy.next

# @lc code=end

