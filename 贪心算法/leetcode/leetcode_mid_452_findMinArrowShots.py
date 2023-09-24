class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[1])
        _, right = points[0]

        res = 1
        for index in range(1, len(points)):
            now_left, now_right = points[index]
            if now_left > right:
                right = now_right
                res += 1
        
        return res