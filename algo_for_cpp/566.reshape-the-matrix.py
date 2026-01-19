#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#
from typing import List
# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n!=r*c:
            return mat
        arr = [x for row in mat for x in row]
        return [arr[i*c:(i+1)*c] for i in range(r)]

# @lc code=end

