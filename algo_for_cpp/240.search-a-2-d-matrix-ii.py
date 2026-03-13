#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 在一个从左往右递增的行
        # 在一个从上往下递增的列
        # 快速的找到我们需要的target
        # 有序的数组就是好数组
        # 所以我们最好不要行列硬性的遍历
        # 我的想法是快速定位他在那几行
        # 然后就可以变成一个线性的部分了
        # 直接开搞
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = n - 1   # 从右上角开始

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1      # 太大了，往左
            else:
                i += 1      # 太小了，往下

        return False
# @lc code=end

