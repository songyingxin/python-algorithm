
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        m = len(nums1)
        n = len(nums2)

        res = 0

        dp = [
            [0] * n for _ in range(m)
        ]  # dp[i][j]: 以下标 i,j 结尾时的最大公共子数组长度

        # 初始化边界
        for i in range(m):
            if nums2[0] == nums1[i]:
                dp[i][0] = 1
                res = max(res, dp[i][0])
        
        # 初始化边界
        for i in range(n):
            if nums1[0] == nums2[i]:
                dp[0][i] = 1
                res = max(res, dp[0][i])
        
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                res = max(res, dp[i][j])
        
        return res



class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        m = len(nums1) + 1
        n = len(nums2) + 1

        dp = [
            [0] * n for i in range(m)
        ]

        res = 0
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

                res = max(res, dp[i][j])
        return res

