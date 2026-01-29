#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # def isBadVersion(version: int) -> bool:
    #     if version >=1:
    #         return True
    #     else:
    #         return False
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        ans = 1  # 处理“全是 0”的情况
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                ans = mid        # 记录一个可能答案
                right = mid - 1  # 继续往左找更早的 1
            else:
                left = mid + 1   # 0 的话，分界线在右边

        return ans

# @lc code=end
set = Solution()
print(set.firstBadVersion(2))
