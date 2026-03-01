#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s=list(s)
        
        for start in range(0, n, 2*k):
            l = start
            r = min(start + k - 1, n - 1)
            
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        
        return "".join(s)
# @lc code=end

