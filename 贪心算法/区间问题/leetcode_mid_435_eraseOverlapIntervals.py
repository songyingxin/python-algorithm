class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        res = 0
        right = intervals[0][1]
        for num in intervals[1:]:
            if num[0] < right:
                res += 1
            else:
                right = num[1]
        
        return res

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        res = 0
        pre = intervals[0]
        for num in intervals[1:]:
            if num[0] == pre[0]:
                pre[1] = min(num[1], pre[1])
                res += 1
                continue
            
            if num[0] >= pre[1]:
                pre = num
            else:
                res += 1
                pre[1] = min(num[1], pre[1])

        
        return res