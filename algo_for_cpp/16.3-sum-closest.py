#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n= len(nums)
        distance = float('inf')
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum != target:
                    if abs(sum - target) < abs(distance):
                        distance = sum - target
                        res = sum
                    if sum < target:
                        left += 1
                    if sum > target:
                        right -= 1
                if sum == target:
                    return target
        return res
# @lc code=end

