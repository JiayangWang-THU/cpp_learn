#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 这次是含有冷冻期
        # 但是不是单次买卖了
        # 现在我们可以进行多次进出
        # 但是只能同时持有一股
        # 如果原来贪心是吧所有的上升期都吃进去
        # 这道题就对你原来吃无脑吃上升期有了惩罚
        # 你今天因为吃小的上升期，可能会因此丢掉next day 的大额上升
        # 所以这道题不再是一个单纯的贪心问题
        # 涉及到max，又有点像dp了
        n = len(prices)
        if n == 0:
            return 0
        # 我们定义三个状态
        # 第 i 天结束后，手里持股时的最大利润
        # 第 i 天结束后，今天刚卖出的最大利润
        # rest[i]：第 i 天结束后，空仓且可买的最大利润
        hold = [0] * n
        sold = [0] * n
        rest = [0] * n
        # 初始化状态
        hold[0] = -prices[0]
        sold[0] = float('-inf')
        rest[0] = 0

        for i in range(1, n):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
            sold[i] = hold[i - 1] + prices[i]
            rest[i] = max(rest[i - 1], sold[i - 1])

        return max(sold[n - 1], rest[n - 1])
# @lc code=end

