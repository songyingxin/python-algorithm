

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break

                left = stack[-1]
                now_width = i - left - 1
                now_height = min(height[left], height[i]) - height[top]
                ans += now_width * now_height
            stack.append(i)
        return ans     
