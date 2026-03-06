#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        if word[1].isupper():
            # 必须全大写
            for c in word:
                if not c.isupper():
                    return False
        else:
            # 后面必须全小写
            for i in range(1, len(word)):
                if not word[i].islower():
                    return False
        
        return True
                            
# @lc code=end

