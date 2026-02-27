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
        # nxt表示按照原始的链条往下走，因为会涉及到断链
        # 所以需要每轮循环就要把正常的路径取保存下来
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

