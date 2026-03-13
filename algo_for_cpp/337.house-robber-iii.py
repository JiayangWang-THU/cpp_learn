#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # base case 走到头了
            if not node:
                return [0,0]
            # 把任务派给left和right
            left = dfs(node.left)
            right = dfs(node.right)
            # 如果rob这个node，那么左右child就不rob
            rob = node.val + left[1] + right[1]
            # 如果不rob这个点，那么我就可以rob他的left 和right，
            not_rob =  (max(left[0], left[1])+ 
                        max(right[0], right[1])
                        )
            return [rob, not_rob]
        return max(dfs(root))
# @lc code=end

