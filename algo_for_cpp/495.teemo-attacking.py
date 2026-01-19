#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#
from typing import List
# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        timeSeries.sort()
        for i in range(len(timeSeries)):
            timeSeries[i] = [timeSeries[i], timeSeries[i] + duration-1]
        total = 0
        out = []
        cur_l = cur_r = timeSeries[0][0]
        for l,r in timeSeries:
            if l <= cur_r:
                cur_r =max(cur_r,r)
            else:
                total += cur_r - cur_l + 1
                out.append([cur_l,cur_r])
                cur_l, cur_r = l, r
        if duration > 0:
            return total+ cur_r - cur_l + 1
        return 0
def main():
    sol=Solution()
    timeSeries = [1,4]
    duration = 2
    print(sol.findPoisonedDuration(timeSeries,duration))
    return 0
if __name__ == "__main__":
    main()
# @lc code=end

