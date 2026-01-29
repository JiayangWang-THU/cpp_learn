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
        #root为0代表见底了，stack为空代表存起来的路径也用完了
        while root or stack:
                # push入栈模拟递，pop出栈模拟归
                # 一直往左走，直到无路可走，把所有的left都压入栈
                while root:
                    stack.append(root)
                    root = root.left
                #root 为空了，left全走完了，现在往回弹出最后一个left，存进去
                #回退，访问节点
                root = stack.pop()
                res.append(root.val)
                # 走右边
                # 转向右子树
                root = root.right
        return res
set = Solution()
print(set.inorderTraversal(TreeNode(1,None,TreeNode(2,TreeNode(3),None))))

        
# @lc code=end

