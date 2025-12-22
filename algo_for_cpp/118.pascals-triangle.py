#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        if numRows >=3:
            res= [[1], [1,1]]
            row_last = [1,1]
            for i in range(3,numRows+1):
                row_now = [0]*i
                for j in range(i):
                    if j==0 or j== i-1:
                        row_now[j] = 1
                    else:
                        row_now[j] = row_last[j-1]+row_last[j]
                    
                row_last = row_now
                res.append(row_last)
            return res
if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))


# @lc code=end

