
import heapq
import collections

# 精简代码


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
