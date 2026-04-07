class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        if target < 3:
            return []

        res = []

        left = 1
        right = 2

        now_sum = 3
        while right < target:
            if now_sum == target:
                res.append([i for i in range(left, right+1)])
                now_sum -= left
                left += 1
            elif now_sum < target:
                right += 1
                now_sum += right
            else:
                now_sum -= left
                left += 1

        return res




        