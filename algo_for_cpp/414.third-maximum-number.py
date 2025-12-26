#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        F=S=T=None
        for n in nums:
            if n==F or n==S or n==T:
                continue
            if F is None or n>F:
                T=S
                S=F
                F=n
            elif S is None or n>S:
                T=S
                S=n
            elif T is None or n>T:
                T=n
        return T if T is not None else F

# @lc code=end

    #  nums.sort(reverse=True)
    #     s = set(nums)
    #     if len(s) < 3:
    #         return max(s)
    #     else:
    #         ss = list(s)
    #         ss.sort(reverse=True)
    #         return ss[2]