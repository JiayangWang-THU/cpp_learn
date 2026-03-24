#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)  # 2. 在这里加上装饰器，它会自动缓存 dfs(i, j) 的结果，避免重复计算
        def dfs(i, j):
            # p走完了，只有s也走完才算匹配
            if j == len(p):
                return i == len(s)

            # 当前这一位是否匹配
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # 如果下一位是*
            if j + 1 < len(p) and p[j + 1] == '*':
                # 两种情况：
                # 1. 这个字符出现0次 -> 跳过 p[j] 和 '*'
                # 2. 当前匹配成功，则让 * 吃掉 s[i]，p位置不动
                return dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                # 普通情况：当前匹配，且一起往后走
                return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)
# @lc code=end

