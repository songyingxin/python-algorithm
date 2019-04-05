class Solution:
    def subsets(self, nums):
        result = []
        item = []
        result.append(item)

        def generate(index, nums, item, result):
            if index >= len(nums):
                return
            
            new_item = item.copy()
            new_item.append(nums[index])  
            result.append(new_item)
            
            generate(index+1, nums, new_item, result)
            generate(index + 1, nums, item, result)
        
        generate(0, nums, item, result)
        return result

if __name__ == "__main__":
    nums = [1,2,3]

    print(Solution().subsets(nums))
