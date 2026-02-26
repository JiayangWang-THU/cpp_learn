#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val}->{self.next}"
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1) 快慢指针找中点并断开
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None  # 断开为两段：head..prev 与 slow..end

        # 2) 递归排序两段
        left = self.sortList(head)
        right = self.sortList(slow)

        # 3) 合并两个有序链表
        return self._merge(left, right)

    def _merge(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a if a else b
        return dummy.next


def main():
    sol = Solution()
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(sol.sortList(head))  # 1->2->3->4->None


if __name__ == "__main__":
    main()
# @lc code=end

