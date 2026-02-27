#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # n %2天生把奇偶合并了，走不到最中间那个
        # 写的比较low

        # n = len(s)
        # if n % 2 ==0:
        #     for i in range(n//2):
        #         s[i],s[n-i-1]=s[n-i-1],s[i]
        # else :
        #     for i in range(n//2):
        #         if i == n//2 + 1:
        #             s[i]=s[i]
        #             break
        #         else:
        #             s[i],s[n-i-1]=s[n-i-1],s[i]
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
# @lc code=end

