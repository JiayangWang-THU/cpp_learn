#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # 找最大的子数组product，这里的子数组主要是保证元素的连贯性

        # 这里主要是负数难处理，所以我们维护两个量，因为负数可以翻转，可以把min变max的潜力
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        for i in range(1, n):
            num = nums[i]

            temp_max = max(num, max_prod*num, min_prod*num)
            temp_min = min(num, max_prod*num, min_prod*num)

            max_prod = temp_max
            min_prod = temp_min

            ans = max(ans, max_prod)

        return ans
# @lc code=end

