#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 位运算的题
        # 先逐位做异或
        # 然后统计1的数量即可
        return bin(x^y).count('1')
# @lc code=end

