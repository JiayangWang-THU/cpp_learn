#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 这道题可以看到的是，由于短板效应，height = min（l，r）
        # 然后短板要往中间移动，移动的过程中，如果中间的比他短，那么他一定会变小，毕竟相当于宽度减少了，高度也减少了
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0
        while left<right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return max_area
# @lc code=end

