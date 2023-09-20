class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        m = len(nums1) + 1
        n = len(nums2) + 1

        dp = [
            [0] * n for i in range(m)
        ]

        for i in range(1, m):
            for j in range(1, n):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]