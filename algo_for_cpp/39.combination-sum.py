#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # two sum 的plus版本
        # 也就是要用已有的数任意组合出target
        # 这里麻烦的点主要在于一个数的使用次数是不设限制的
        # 可能性比较多
        # 看着有点像dp
        # 但是dp适合求值
        # 回溯适合求方法数
        res = []
        path = []

        def dfs(start, remain):
            # 终止条件1：刚好凑出
            if remain == 0:
                res.append(path[:])
                return
            
            # 终止条件2：超了
            if remain < 0:
                return
            
            # 从 start 开始选，避免重复组合
            for i in range(start, len(candidates)):
                num = candidates[i]
                
                # 做选择
                path.append(num)
                
                # 因为可以重复使用当前数，所以还是传 i
                dfs(i, remain - num)
                
                # 撤销选择
                path.pop()

        dfs(0, target)
        return res
# @lc code=end

