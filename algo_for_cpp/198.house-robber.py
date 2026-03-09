#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 给一个nums
        # adjacent house抢不了
        # 只能跳着来，问我怎么个抢法收益最高
        # 主要麻烦的点是他跳的格子数量是不确定的
        # 你抢这一家会影响下一家能不能抢
        # 所以这题是dp
        # 记dp[i]作为到第i家为止的max profits
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
# @lc code=end

