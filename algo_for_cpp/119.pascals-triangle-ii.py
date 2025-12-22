#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex >=2:
            row_last = [1,1]
            for i in range(2,rowIndex+1):
                row_now = [0]*(i+1)
                for j in range(0,i+1):
                    if j==0 or j == i:
                        row_now[j] = 1
                    else:
                        row_now[j] = row_last[j-1]+row_last[j]
                row_last = row_now
            return row_last
# @lc code=end

