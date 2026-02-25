#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 对于链表的删除，实际上就是指针跳过
        # 这里我们引入两个指针p1和p2，可以类比更新数组的快慢双指针思路
        # 快指针用于比较当前node的val，慢指针用来更新最后实际的链表
        # p1是快指针的话，p2是慢指针
        dummy = ListNode(0)
        p2 = dummy
        p1 = head
        while p1:
            p2.next = p1
            p2 = p2.next
            while p1.next and p1.val == p1.next.val:
                p1 = p1.next
            p1 = p1.next
        #适时断尾
        p2.next = None
        return dummy.next
# @lc code=end

