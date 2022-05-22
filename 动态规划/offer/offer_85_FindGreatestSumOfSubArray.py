



class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> List[int]:
        # write code here
        dp = [i for i in array]
        max_len = 1
        start, end = 0, 1
        max_start, max_end  = 0, 1
        max_sum = array[0]

        for i in range(1, len(array)):
            end += 1
            dp[i] = max(dp[i-1]+array[i], array[i])

            if dp[i-1] + array[i] < array[i]:
                start, end = i, i+1

            if dp[i] > max_sum or (dp[i]== max_sum and (end-start)>max_len):
                max_start = start
                max_end = end
                max_len = end - start
                max_sum = dp[i]
        return array[max_start:max_end]