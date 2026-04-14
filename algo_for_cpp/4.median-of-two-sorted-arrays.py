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
        # new_list = sorted(nums1 + nums2)
        # return (new_list[len(new_list) // 2] + new_list[(len(new_list) - 1) // 2]) / 2

        # 这题也可以用递归的方法
        m = len(nums1)
        n = len(nums2)
        total = m + n
        self.index1 = 0
        self.index2 = 0
        def find_kth(nums1,nums2,k):
            # 第一种情况，index1走到m了
            if self.index1 == m:
                return nums2[self.index2 + k - 1]
            # 第二种情况，index2走到n了
            if self.index2 == n:
                return nums1[self.index1 + k - 1]
            # 第三种情况，两个指针都还没走到末尾
            if k == 1:
                return min(nums1[self.index1], nums2[self.index2])
            # 递归查找第k小的元素
            half_k = k // 2
            new_index1 = min(self.index1 + half_k, m) - 1
            new_index2 = min(self.index2 + half_k, n) - 1
            if nums1[new_index1] < nums2[new_index2]:
                self.index1 = new_index1 + 1
            else:
                self.index2 = new_index2 + 1
            return find_kth(nums1, nums2, k - half_k)
        if total % 2 == 1:
            return find_kth(nums1, nums2, total // 2 + 1)
        else:
            return (find_kth(nums1, nums2, total // 2) + find_kth(nums1, nums2, total // 2 + 1)) / 2
# @lc code=end

