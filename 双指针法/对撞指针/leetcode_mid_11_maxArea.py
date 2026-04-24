class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        max_area = 0
        while left < right:
            area = (right-left) * min(height[right], height[left])
            max_area = max(max_area, area)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return max_area