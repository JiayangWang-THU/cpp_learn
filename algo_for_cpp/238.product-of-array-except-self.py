#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 限制时间复杂度O(n)那就没办法双for暴力法了
        # 限制了不让用除法，那也没办法一开始全部×起来再div了
        n = len(nums)
        left = [1] * n
        right = [1] * n
        ans = [1] * n


        # 线性的问题，还限制时间复杂度
        # 大概率需要用到分治的思想
        # 而且还需要空间换时间，也就是需要存下来一些算过的值
        # 这里建模建的是 product all except myself
        # 那就是我所有左边的乘积和我所有右边的乘积
        # 两个数组left和right扫一遍就知道 i 左边和右边的乘积了
        # 最后进行合并
        # left[i] = nums[i] 左边所有数的乘积
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # right[i] = nums[i] 右边所有数的乘积
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # 合并
        for i in range(n):
            ans[i] = left[i] * right[i]

        return ans
# @lc code=end

