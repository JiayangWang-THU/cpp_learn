#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 返回的是一个字典
        freq = Counter(nums)
        
        heap = []
        # python只有小根堆
        # 如果要换成大根堆就得自己手动转负数再送进去
        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))
        
        ans = []
        for _ in range(k):
            count, num = heapq.heappop(heap)
            ans.append(num)
        
        return ans
# @lc code=end

