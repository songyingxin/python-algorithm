# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        small = 1
        big = 2

        results = []
        while small < tsum // 2 + 1:
            list_now = list(range(small, big+1))
            if sum(list_now) == tsum:
                results.append(list_now)
                big += 1
            elif sum(list_now) > tsum:
                small += 1
            else:
                big += 1

        return results

if __name__ == "__main__":
    
    tsum = 3
    Solution().FindContinuousSequence(3)
