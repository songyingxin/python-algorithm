class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        left,right = intervals[0]

        for index in range(1, len(intervals)):
            now_left, now_right = intervals[index]
            if now_left > right:
                res.append([left, right])
                left = now_left
                right = now_right
            else:
                right = max(right, now_right)
        
        res.append([left, right])

        return res