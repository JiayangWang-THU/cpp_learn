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
            # 把我们的映射简记为f(x)
            # 输入是具体的逐个数字num
            # 输出是index - 1
            # 负号用于标记是否出现过
            # abs用于去掉负号的影响，避免干扰映射
            # 假如我们第一个数字是4
            # 根据映射关系 4 -> 第四个 -> index = 4-1=3
            # 所以我们把第三个位置取反
            # 这样就建立了num和index的关系，如果还有正数，就是刚好那个index没有找到数字
            # 最后统计正数就行，index就是 nums -1  
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

