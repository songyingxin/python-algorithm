


class Solution:
    def FindContinuousSequence(self , sum: int) -> List[List[int]]:
        # write code here
        left = 1
        right = 2
        res = []

        while left < right:
            cur_sum = (left + right) * (right-left+1) / 2

            if cur_sum == sum:
                res.append(list(range(left, right+1)))
                left += 1
            elif cur_sum < sum:
                right += 1
            else:
                left += 1
        
        return res