#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0

        def dfs(node):
            if not node:
                return

            # 1. 先右（更大的值）
            dfs(node.right)

            # 2. 更新当前节点
            self.total += node.val
            node.val = self.total

            # 3. 再左（更小的值）
            dfs(node.left)

        dfs(root)
        return root
# @lc code=end

