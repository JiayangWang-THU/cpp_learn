#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 组相似
        # 给一个列表
        # 里面有若干字符串
        # 分成几组
        # 实际上我感觉还是hash表统计字母的频率就行
        # 频率元组学习一手
        # groups = {}

        # for s in strs:
        #     count = [0] * 26
        #     for ch in s:
        #         count[ord(ch) - ord('a')] += 1
        #     # 把这个元组当成key
        #     key = tuple(count)

        #     if key not in groups:
        #         groups[key] = []
        #     groups[key].append(s)

        # return list(groups.values())
        groups = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())
# @lc code=end

