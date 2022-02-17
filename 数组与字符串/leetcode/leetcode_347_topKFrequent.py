
import heapq
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_times = {}
        for val in nums:
            num_times[val] = 1 if val not in num_times else num_times[val] +1
        nums_list = [[key,val] for key,val in num_times.items()]
        result = heapq.nlargest(k, nums_list, key=lambda x: x[1])
        result = [val[0] for val in result]
        return result

# 精简代码


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
