#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 维护一个滑动窗口的最大值
        # 看看这个窗口，大小是恒定的
        # 只需要一次线性扫描就够用了
        # 每次取里面的max or min
        # 这窗口本身遵循先进先出，后进后出
        # 所以我感觉主要像队列的知识
        n = len(nums)
        if n<=k:
            return [max(nums)]
        
        res = []
        # i+2 <=n-1
        # i<=n-3
        for i in range(n - k + 1):
            res.append(max(nums[i:i+k]))
        return res

# @lc code=end

