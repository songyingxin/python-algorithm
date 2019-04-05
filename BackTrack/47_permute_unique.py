class Solution:
    def permuteUnique(self, nums):
        result = []
        item = []
        nums = sorted(nums)
        self.back_track(nums, item, result)
        return result

    def back_track(self, nums, item, result):

        if len(item) == len(nums):
            vals = [nums[i] for i in item]
            if vals not in result:
                result.append(vals )
            return

        for i in range(len(nums)):
            if i not in item:
                new_item = item.copy()
                new_item.append(i)
                self.back_track(nums, new_item, result)

if __name__ == "__main__":
    
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))
