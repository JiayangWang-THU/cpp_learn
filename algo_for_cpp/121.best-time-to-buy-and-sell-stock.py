#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 开始炒股
        # 我知道的是一个数组prices
        # index表示是第i天的stock
        # 可以 买入 + 卖出多次
        # 同一时间只能持有一股
        # 必须先买后卖
        # 求max
        # 没有profit就return 0
        # 我们维护的是一个前缀min(prices[0 ... i])
        min_price = float('inf')
        max_profit = 0
        # 这里遍历的过程天然的带着时序
        # 所以我们只要一直维护整个min就行
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
# @lc code=end

