#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 找回文子串
        # 还只要一个最长
        # 之前学过找所有回文串的可能
        # 当时是用的中心扩展法
        # 现在只要最长的，所以可以在扩展的过程中记录最长的
        longest = ""
        for i in range(len(s)):
            # 奇数长度的回文串
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1
            
            # 偶数长度的回文串
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1
        return longest

# @lc code=end

