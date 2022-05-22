# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> int:
        # write code here
        # dp[i]: 以i结尾的子数组的和的最大值
        # dp[i] = max(dp[i-1]+num[i], num[i])
        
        dp = [0] * len(array)
        
        max_len = array[0]
        max_len_array = [array[0]]

        dp[0] = array[0]
        for i in range(1, len(array)):

            dp[i] = max(dp[i-1]+array[i], array[i])
        
        return max(dp)


if __name__ == "__main__":
    
    print(Solution().FindGreatestSumOfSubArray([6, -3, -2, 7, -15, 1, 2, 2]))
