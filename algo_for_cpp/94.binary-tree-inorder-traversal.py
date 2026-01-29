#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
from typing import Optional, List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left->root->right
        res = []
        stack = []
        def in_order(root: TreeNode | None):
            """中序遍历"""
            if root is None:
                return
            # 访问优先级：左子树 -> 根节点 -> 右子树
            in_order(root=root.left)
            res.append(root.val)
            in_order(root=root.right)
        in_order(root)
        return res
set = Solution()
print(set.inorderTraversal(TreeNode(1,None,TreeNode(2,TreeNode(3),None))))

        
# @lc code=end

