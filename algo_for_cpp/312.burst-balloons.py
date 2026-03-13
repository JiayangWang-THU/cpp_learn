#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 先审题
        # 0-n-1个气球
        # 每个气球带权重nums
        # 打第i个气球就会得到三连击的coins
        # 如果越界就当基底1
        # 感觉打气球有点像动态规划问题，有明显的递推
        # 一个气球的收益，不是固定的
        #而是取决于它什么时候被戳
        arr = [1] + nums + [1]
        n = len(arr)

        dp = [[0] * n for _ in range(n)]

        # length 表示区间长度
        for length in range(2, n):   # 至少要留出一个开区间
            for i in range(0, n - length):
                j = i + length

                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                    )

        return dp[0][n - 1]
# @lc code=end

