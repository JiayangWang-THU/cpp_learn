#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n

        def dfs(path):
            if len(path) == n:
                res.append(path[:])   # 复制一份
                return

            for i in range(n):
                if used[i]:
                    continue

                # 选择 nums[i]
                path.append(nums[i])
                used[i] = True

                # 递归进入下一层
                dfs(path)

                # 回溯
                path.pop()
                used[i] = False

        dfs([])
        return res
# @lc code=end

