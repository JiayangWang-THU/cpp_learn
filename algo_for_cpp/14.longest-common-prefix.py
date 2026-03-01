#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        for i in range(len(first)):
            for s in strs[1:]:
                # 越界 或 不匹配
                if i >= len(s) or s[i] != first[i]:
                    return first[:i]

        return first
        
            
# @lc code=end

