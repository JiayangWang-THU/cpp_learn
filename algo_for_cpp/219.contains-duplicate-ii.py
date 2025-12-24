#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_pos = dict()
        for i, x in enumerate(nums):
            if x in last_pos and i - last_pos[x]<=k:
                return True
            last_pos[x] = i 
        return False
# @lc code=end

