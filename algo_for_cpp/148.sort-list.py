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
        cur = head
        while cur.next :
            if cur.val >= cur.next.val:
                zhongzhuan = cur.val
                cur.val =cur.next.val
                cur.next.val =zhongzhuan
                cur = cur.next
            else:
                cur = cur.next
                continue
            
        return head.next
def main():
    sol = Solution()
    head = ListNode(4,ListNode(2,ListNode(1,ListNode(3))))
    print(sol.sortList(head))

if __name__ == "__main__":
    main()
# @lc code=end

