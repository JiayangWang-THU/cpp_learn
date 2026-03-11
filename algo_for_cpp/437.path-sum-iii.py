#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 原来是two num 等于target
        # 暴力扫描总能找到
        # 现在数据结构是树了
        # 我想的是肯定要dfs了
        # 我们来思考一下dfs如何构造
        # 这里甚至会用到双dfs
        def countFrom(node, target):
            if not node:
                return 0

            res = 1 if node.val == target else 0
            res += countFrom(node.left, target - node.val)
            res += countFrom(node.right, target - node.val)
            return res

        if not root:
            return 0

        return (
            countFrom(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
# @lc code=end

