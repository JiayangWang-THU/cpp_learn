#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            cha = target - num
            
            # 检查“差值”是否已经在字典里
            if cha in dic:
                # 如果在，返回差值的下标和当前数字的下标
                return [dic[cha], i]
            
            # 2. 如果不在，把当前数字作为 key，下标作为 value 存入字典
            dic[num] = i
    
        
# @lc code=end

