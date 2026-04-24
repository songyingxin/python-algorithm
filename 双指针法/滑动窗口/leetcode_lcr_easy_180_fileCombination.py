class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        
        sum_val = 1
        left = 1
        right = 1
        res = []
        while right < target:
            if sum_val < target:
                right += 1
                sum_val += right
            elif sum_val > target:
                sum_val -= left
                left += 1
            else:
                if right!=left:
                    nums = [i for i in range(left, right+1)]
                    res.append(nums)
                sum_val -= left
                left += 1
        
        return res