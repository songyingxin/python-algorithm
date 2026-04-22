

# 动态规划
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        # 【改动1】left数组：存「左边最高的柱子高度」（不是索引）
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        # 【改动2】right数组：存「右边最高的柱子高度」（不是索引）
        right_max = [0] * n
        right_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # 【改动3】直接按格累加雨水（唯一正确公式）
        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        
        return res