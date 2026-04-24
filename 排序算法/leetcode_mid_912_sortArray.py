import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quick_sort(arr):
            if len (arr) < 2:
                return arr
                
            n = len(arr)-1
            pivot_idx = random.randint(0, n)  # 随机快排
            pivot = arr[pivot_idx]
            
            # 双指针遍历 left-right 区间
            left_arr = []
            right_arr = []
            mid_arr = []
            
            for num in arr:
                if num > pivot:
                    right_arr.append(num)
                elif num == pivot:
                    mid_arr.append(num)
                else:
                    left_arr.append(num)

            left_arr = quick_sort(left_arr)
            right_arr = quick_sort(right_arr)
            return left_arr + mid_arr + right_arr
        
        return quick_sort(nums)