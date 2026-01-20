#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     if nums[i] % 2 != 0:
        #         for j in range(i+1,len(nums)):
        #             if nums[j] %2 == 0:
        #                 nums[i],nums[j] = nums[j],nums[i]
        #                 break
        # return nums
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] % 2 == 0:
                l += 1
            while l < r and nums[r] % 2 == 1:
                r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        return nums
# @lc code=end

