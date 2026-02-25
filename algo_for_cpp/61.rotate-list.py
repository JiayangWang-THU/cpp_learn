#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(head):
            length = 0
            cur = head
            while cur:
                length += 1
                cur = cur.next
            return length

        def rotate_right_once(head):
            if not head or not head.next:
                return head
            prev = None
            cur = head
            while cur.next:
                prev = cur
                cur = cur.next
            prev.next = None
            cur.next = head
            return cur

        n = get_length(head)
        if n == 0:
            return head

        k %= n
        for _ in range(k):
            head = rotate_right_once(head)

        return head
# @lc code=end

