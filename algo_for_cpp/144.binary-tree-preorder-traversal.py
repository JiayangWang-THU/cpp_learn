#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # root -> left ->right
        res= []
        stack = []
        def dfs_preorder(root:Treenode|None):
            """前序遍历"""
            if root is None:
                return
            # 访问优先级：根节点 -> 左子树 -> 右子树
            res.append(root.val)
            dfs_preorder(root=root.left)
            dfs_preorder(root=root.right)
        dfs_preorder(root)
        return res
# @lc code=end

