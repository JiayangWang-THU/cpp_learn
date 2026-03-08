#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        max_size = 0

        def is_all_one(i,j,k):
            for x in range(i,i+k):
                for y in range(j,j+k):
                    # 注意此处的matrix里面的元素都是字符串
                    if matrix[x][y]!="1":
                        return False
            return True
        
        for i in range(m):
            for j in range(n):
                cur_max = min(m-i,n-j)
                for k in range(1,cur_max+1):
                    if is_all_one(i,j,k):
                        max_size = max(max_size,k)
        return max_size*max_size
# @lc code=end

