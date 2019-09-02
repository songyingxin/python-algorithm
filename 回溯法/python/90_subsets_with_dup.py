class Solution:
    def subsetsWithDup(self, nums) :
        result = []
        item = []
        result.append(item)
        nums= sorted(nums)
        self.back_track(nums, 0, item, result)
        return result

    def back_track(self, nums, index, item, result):

        if index >= len(nums):
            return
        
        new_item = item.copy()
        new_item.append(nums[index])
        if new_item not in result:
            result.append(new_item)
        self.back_track(nums, index + 1, new_item, result )
        self.back_track(nums, index+1, item, result)

if __name__ == "__main__":
    
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))
