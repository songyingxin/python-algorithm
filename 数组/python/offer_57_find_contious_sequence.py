# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        small = 1
        big = 2
        sum_val = small + big
        results = []
        while small < tsum // 2 + 1:
            list_now = list(range(small, big+1))
            if sum_val == tsum:
                results.append(list_now)
                big += 1
                sum_val += big
            elif sum_val > tsum:
                sum_val -= small
                small += 1
            else:
                big += 1
                sum_val += big

        return results
        
if __name__ == "__main__":
    
    tsum = 3
    Solution().FindContinuousSequence(3)
