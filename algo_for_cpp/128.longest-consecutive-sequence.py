#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for x in num_set:

            # 只有序列起点才开始扩展
            if x - 1 not in num_set:

                cur = x
                length = 1

                while cur + 1 in num_set:
                    cur += 1
                    length += 1

                longest = max(longest, length)

        return longest
# @lc code=end

