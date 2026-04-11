

class Solution:
    def makesquare(self, nums: List[int]) -> bool:

        def dfs(item, start_index):
            if start_index >= len(nums):
                return item[0] == item[1] ==item[2] ==item[3] == self.square
            
            for i in range(4):
                if item[i] + nums[start_index] > self.square:
                    continue

                item[i] += nums[start_index]

                if dfs(item, start_index+1):
                    return True
                
                item[i] -= nums[start_index]
            
            return False

        if len(nums) < 4:
            return False
        
        square_sum = sum(nums)

        if square_sum % 4 != 0:
            return False
        
        self.square = square_sum // 4
        for val in nums:
            if val > self.square:
                return False
        nums.sort(reverse=True)
        item = [0] * 4

        return dfs(item, 0)



        



