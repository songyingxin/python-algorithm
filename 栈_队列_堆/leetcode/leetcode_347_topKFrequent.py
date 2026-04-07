
import heapq
import collections

# 精简代码


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        help_dict = collections.Counter(nums)
        
        help_dict = [[key,val] for key,val in help_dict.items()]
        help_dict = sorted(help_dict, key=lambda x:x[1])[::-1]
        res = [val[0] for val in help_dict[:k]]
        return res