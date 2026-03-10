#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 只出现一次的数字
        # 题目要求线性复杂度
        # 所以肯定不能.count一个个统计次数了
        # 最直观的想法还是hash表
        # freq = {}
        # for x in nums:
        #     if x in freq:
        #         freq[x]=freq[x]+1
        #     else:
        #         freq[x]=1
        # for k, v in freq.items():
        #     if v == 1:
        #         return k
        # 但是这道题一定有巧办法
        # 那就是我之前鼓捣过的差集法
        # 先求原列表的和
        sum_2 = 0
        for x in nums:
            sum_2=x+sum_2
        # sum_2=1+2+2+2...
        set_nums=set(nums)

        sum_1 = 0
        for x in set_nums:
            sum_1=x+sum_1
        return -(sum_2-2*sum_1)
# @lc code=end

