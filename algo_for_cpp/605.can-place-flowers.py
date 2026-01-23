#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new = [0] + flowerbed + [0]
        cnt = 0
        for i in range(1,len(new)-1):
            if new[i-1]==0 and new[i]==0 and new[i+1]==0:
                new[i]=1
                cnt+=1
        return cnt>=n
# @lc code=end

