#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt =dict()
        for n in nums:
            cnt[n]=cnt.get(n,0)+1
            if cnt[n]>1:
                return True
        return False
            # @lc code=end

