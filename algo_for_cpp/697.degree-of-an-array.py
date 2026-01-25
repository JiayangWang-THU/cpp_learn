#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        max_freq = max (cnt.values())
        keys = [k for k, v in cnt.items() if v == max_freq]
        min_len = []
        for key in keys:
            first = nums.index(key)
            last = len(nums) - 1 - nums[::-1].index(key)
            length = last - first + 1
            min_len.append(length)
        min_len = min(min_len)
        return min_len
# @lc code=end

