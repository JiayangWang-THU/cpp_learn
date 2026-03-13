#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        # 找到最少数量的完全平方数相加等于n
        # least
        # 确实一眼动态规划
        # 面向结果吧，dp[i] = 凑出数字 i 所需的最少完全平方数个数
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                # 凑成 i 的最优解，
                # 等于“凑成剩余部分”的最优解，再加上最后选的一个平方数。
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]
# @lc code=end

