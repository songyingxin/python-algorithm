class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        res = 0
        right = intervals[0][1]
        for index in range(1, len(intervals)):
            now_left, now_right = intervals[index]
            if now_left < right:
                res += 1
            else:
                right = now_right
        
        return res