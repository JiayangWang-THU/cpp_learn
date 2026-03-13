#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 只让用常数的extra space
        # 这就不让我们用set了
        # 又想到了我的差集法
        
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
# @lc code=end

