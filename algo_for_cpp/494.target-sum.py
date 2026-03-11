#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 目标就是找到target的路径
        # 这一题的step比较复杂
        # step的集合应该是所有的nums的±状态
        # 我们还是可以用dp
        # 只是这次是统计次数了
        dp = defaultdict(int)
        dp[0] = 1   # 还没选任何数时，和为 0 的方案数是 1

        for x in nums:
            new_dp = defaultdict(int)
            for s, cnt in dp.items():
                new_dp[s + x] += cnt
                new_dp[s - x] += cnt
            dp = new_dp

        return dp[target]
# @lc code=end

