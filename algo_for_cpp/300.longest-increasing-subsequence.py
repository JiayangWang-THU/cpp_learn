#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 这题子序列也不需要保证位置连续只需要保证逻辑连续就够了
        # 但是他的问题在于，还是不能进行排序
        # 他还是需要满足相对的位置关系不能发生变化
        # 如果排序了，那相当于肯定都是递增的，就没有意义了

        # 最长，感觉看到这种最的问题就要想到动态规划
        # 然后就是如果需要暴力法，应该怎么暴力呢
        # # 遍历所有的序列
        # n = len(nums)
        # # 这里的dp[i]表示以nums[i]结尾的最长子序列的长度
        # dp = [1]*n
        
        # for i in range(n):
        #     for j in range(i):
        #         # 如果满足了前一个小于后面的，证明可以接上，他就可以把之前接上的部分再加上i这个部分
        #         if nums[j] < nums[i]:
        #             # 最坏的情况还有取自己本身的序列作为保底 
        #             # 只有新添加进来的链子长度变大的时候才更新dp[i]
                    
        #             dp[i] = max(dp[i], dp[j]+1)
                    
        # return max(dp)
        n = len(nums)
        ans = 0

        def dfs(i, path):
            nonlocal ans

            # 走到末尾，更新答案
            if i == n:
                ans = max(ans, len(path))
                return

            # 1) 不选 nums[i]
            dfs(i + 1, path)

            # 2) 选 nums[i]，但必须保持递增
            if not path or nums[i] > path[-1]:
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()   # 回溯

        dfs(0, [])
        return ans
# @lc code=end

