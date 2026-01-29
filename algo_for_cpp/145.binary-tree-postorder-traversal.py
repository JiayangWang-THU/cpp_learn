#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left -> right -> root 
        res=[]
        def dfs_postorder(root:TreeNode|None):
            """后序遍历"""
            if root is None:
                return
            # 访问优先级：左子树 -> 右子树 -> 根节点
            dfs_postorder(root=root.left)
            dfs_postorder(root=root.right)
            res.append(root.val)
        dfs_postorder(root)
        return res
        # @lc code=end

