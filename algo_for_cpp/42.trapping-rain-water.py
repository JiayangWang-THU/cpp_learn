#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        #每个单位木桶能接到的水就等于min（左，右）- 底部高度
        #我们把每一列当成一个独立的桶
        #这里储水量的多少除了和这一格的高度有关系，还和周围两格有关系
        #所以我们需要记录左边和右边的最高高度
        #从左到右遍历一遍，记录每一格左边的最高高度，只是去掉第一个和最后一个
        
        #左边最高
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        # 右边最高
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        water = 0
        for i in range(1,n-1):
            h = min(left_max[i], right_max[i])
            if h > height[i]:
                water += h - height[i]
        return water
            

# @lc code=end

