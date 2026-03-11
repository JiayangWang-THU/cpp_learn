#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
from typing import List

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
            # 找到消失的数字，我们直接建立数组的hash
            # 数字范围是1 到 n
            # 我们建立index 0 到 n-1
            # 所以我们要把所有的数字都映射到index
            for num in nums:
                
                if nums[abs(num) - 1] > 0:
                    nums[abs(num) - 1] = -nums[abs(num) - 1]

            res = []
            for i in range(len(nums)):
                if nums[i] > 0:
                    res.append(i + 1)
            return res

def main():
    sol = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(sol.findDisappearedNumbers(nums))
    return 0
if __name__ == "__main__":
    main()
# @lc code=end

