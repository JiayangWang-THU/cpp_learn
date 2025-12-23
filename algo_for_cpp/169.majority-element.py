#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#


# @lc code=start
#先排序再取中位数
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
# @lc code=end
#直接计数O(n^2)直接超时boom💥
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
            if nums.count(n) > len(nums)//2:
                return n
#使用哈希表计数
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
            if count[n] > len(nums)//2:
                return n
#使用摩尔投票法
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        for n in nums:
            if count == 0:#为0就重新评选候选人
                candidate = n
            count += (1 if n == candidate else -1)
        return candidate