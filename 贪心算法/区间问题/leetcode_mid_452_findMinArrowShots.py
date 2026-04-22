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


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[0])
        right = points[0][1]
        res = 1

        for index in range(1, len(points)):
            now_left, now_right = points[index]
            if now_left > right:
                res += 1
                right = now_right
            else:
                right = min(right, now_right)
        return res