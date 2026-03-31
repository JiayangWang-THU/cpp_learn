#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 无重复字符的最长子串
        # 滑动窗口
        left = 0
        right = 0
        longest = 0
        seen = set()
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                longest = max(longest,right-left+1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return longest
# @lc code=end

