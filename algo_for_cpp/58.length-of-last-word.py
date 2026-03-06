#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        #  跳过尾部空格
        while i >= 0 and s[i] == " ":
            i -= 1
        
        #  统计最后一个单词长度
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        return length
# @lc code=end

