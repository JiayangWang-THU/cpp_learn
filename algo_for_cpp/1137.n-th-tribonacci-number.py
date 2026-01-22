#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        if n == 0:
            return t0
        elif n == 1 or n == 2:
            return t1
        for i in range(3,n+1):
            t3 = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = t3
        return t3
# @lc code=end

