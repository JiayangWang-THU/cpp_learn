#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
import sys
from typing import List
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        last = 0
        now = 0
        res = []
        ans = []
        for now in range(1,len(nums)):
            if nums[now]-nums[now-1] != 1 :# 此处可以得到不连续了
                res.append(nums[last:now]) # 存一下从（last-->(now-1）)
                last = now # 更新一下新的子区间
        res.append(nums[last:])
        #格式化输出
        for seg in res:
            if len(seg) == 1:
                ans.append(str(seg[0]))
            else:
                ans.append(f"{seg[0]}->{seg[-1]}")
        return ans

# def main():
#     sol = Solution()
#     nums = [0,2,3,4,6,8,9]
#     print(sol.summaryRanges(nums))
#     return 0
# if __name__ == "__main__":
#     main()
# @lc code=end

