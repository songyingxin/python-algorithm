
# 采用堆来做
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap_max = []
        self.heap_min = []
        self.data_length = 0
        

    def addNum(self, num: int) -> None:
        if self.data_length % 2 == 0:
            if self.data_length > 1 and num < -self.heap_max[0]:
                num = -heapq.heappushpop(self.heap_max, -num)
            heapq.heappush(self.heap_min, num)
        else:
            if self.data_length > 0 and num > self.heap_min[0]:
                num = heapq.heappushpop(self.heap_min, num)
            heapq.heappush(self.heap_max, -num)
        
        self.data_length += 1

    def findMedian(self) -> float:

        if len(self.heap_max) < len(self.heap_min):
            return self.heap_min[0]
        elif len(self.heap_max) == len(self.heap_min):
            return (self.heap_min[0] - self.heap_max[0]) / 2
        else:
            return -self.heap_max[0]