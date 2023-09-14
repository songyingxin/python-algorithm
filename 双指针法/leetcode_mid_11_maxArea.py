class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        res = -1

        while left < right:
            now_val = (right-left) * min(height[left], height[right])
            res = max(now_val, res)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return res
