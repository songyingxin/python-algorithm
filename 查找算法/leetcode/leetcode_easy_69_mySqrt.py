class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        res = 0
        while left <= right:
            mid = (left+right) // 2
            if mid**2 == x:
                return mid
            elif mid ** 2 < x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return res