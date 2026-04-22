
# 堆的思想
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        topn = heapq.nlargest(k, nums)
        return topn[-1]
        