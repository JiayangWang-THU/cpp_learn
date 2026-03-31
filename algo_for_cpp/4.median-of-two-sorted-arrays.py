#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 找两个有序数组的中位数
        # 最简单的就是合并两个数组，然后找中位数
        # 但是时间复杂度是 O(m+n)
        # 可以用二分法来优化
        
        # 取较短的数组进行二分查找
        new_list = sorted(nums1 + nums2)
        return (new_list[len(new_list) // 2] + new_list[(len(new_list) - 1) // 2]) / 2
# @lc code=end

