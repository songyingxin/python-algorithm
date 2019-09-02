class Solution:
    def permute(self, nums):
        result = []
        item = []
        self.back_track(nums, item, result)

        return result
    
    def back_track(self, nums, item, result):

        if len(item) == len(nums):
            result.append(item)    
            return

        for val in nums:
            if val not in item:
                new_item = item.copy()
                new_item.append(val)
                self.back_track(nums, new_item, result)

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))