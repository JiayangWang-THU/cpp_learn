#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]> 0:
                break
            if nums[i]+nums[-1]+nums[-2]<0:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1 
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1               
                if sum < 0:
                    left += 1
                if sum > 0:
                    right -= 1
        return ans
# @lc code=end

