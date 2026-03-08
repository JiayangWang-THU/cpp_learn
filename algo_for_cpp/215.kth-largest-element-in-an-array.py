#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
import heapq
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 数组中的 k th 元素
        # 第一反应肯定还是sort一下
        # nums.sort()
        # return nums[-k]
        # 但是本题题目的意思是希望我们不用sort也可以把结果弄出来
        # 这题让我想到了topk
        # 但是topk需要建一个堆
        heap = nums[:k]
        heapq.heapify(heap)
        for x in nums[k:]:
            if x > heap[0]:
                heapq.heapreplace(heap, x)   # 弹最小的，放入新的

        return heap[0]
# @lc code=end

