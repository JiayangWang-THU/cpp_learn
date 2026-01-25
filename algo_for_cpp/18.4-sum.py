#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]> target:
                break
            if nums[i]+nums[-1]+nums[-2]+nums[-3]<target:
                continue
            for j in range(i+1,n-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i]+nums[j]+nums[j+1]+nums[j+2]> target:
                    break
                if nums[i]+nums[j]+nums[-1]+nums[-2]<target:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1 
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1               
                    if sum < target:
                        left += 1
                    if sum > target:
                        right -= 1
        return ans

# @lc code=end

