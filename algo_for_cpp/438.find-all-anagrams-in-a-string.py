#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 找到和p相似的结构
        # 不在乎顺序
        # 不在乎顺序的题，但会在乎连续性
        # 我在思考，能不能拿个set去遍历整个string
        # 复杂度是O(n)
        # 但是set会丢失次数
        # 被大G老师驳回

        # 这题事实上是滑动窗口
        # 窗口长度为n
        # n, m = len(s), len(p)
        # if n < m:
        #     return []

        # target = Counter(p)
        # res = []
        # # 假如一个长度为n
        # # 窗口长为m
        # # n = 多少个m带重叠
        # # 事实上我们只统计最左边的就行
        # # i+m-1是有边界容易越界
        # # i+m-1<=n-1
        # # 所以i<=n-m
        # # 又range左闭右开
        # for i in range(n - m + 1):
        #     window = Counter(s[i:i+m])
        #     if window == target:
        #         res.append(i)

        # return res
        n, m = len(s), len(p)
        if n < m:
            return []

        cnt = [0] * 26

        # 先把 p 记为 -1，窗口前 m 个字符记为 +1
        for i in range(m):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(p[i]) - ord('a')] -= 1

        # diff = 当前多少个位置非 0
        diff = 0
        for x in cnt:
            if x != 0:
                diff += 1

        res = []
        if diff == 0:
            res.append(0)

        for i in range(m, n):
            x = ord(s[i]) - ord('a')       # 新进来的字符
            y = ord(s[i - m]) - ord('a')   # 移出去的字符

            if x != y:
                # 处理进入字符 x
                if cnt[x] == 0:
                    diff += 1
                cnt[x] += 1
                if cnt[x] == 0:
                    diff -= 1

                # 处理移出字符 y
                if cnt[y] == 0:
                    diff += 1
                cnt[y] -= 1
                if cnt[y] == 0:
                    diff -= 1

            if diff == 0:
                res.append(i - m + 1)

        return res
# @lc code=end

