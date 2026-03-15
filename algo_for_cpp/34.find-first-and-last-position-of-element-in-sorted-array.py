#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 在排序数组种找到第一个位置和最后一个位置
        # 这里限制了复杂度为O(logn)
        # 而且已经排好序了
        # 我的第一反应就是左右分治
        # 肯定不能线性扫描
        # 2logn还是log的复杂度
        def find_left():
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

                if nums[mid] == target:
                    ans = mid

            return ans

        def find_right():
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1

                if nums[mid] == target:
                    ans = mid

            return ans

        return [find_left(), find_right()]

# @lc code=end

