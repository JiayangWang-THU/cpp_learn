#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i in range(len(s)):
            if i + 1 < len(s) and mp[s[i]] < mp [s[i+1]]:
                sum = sum - mp[s[i]]
            else:
                sum = sum + mp[s[i]]
        return sum
# @lc code=end

