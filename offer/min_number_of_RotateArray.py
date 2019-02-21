# -*- coding:utf-8 -*-

# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         # write code here

#         if len(rotateArray)  == 0:
#             return None
        
#         start_one = rotateArray[0]

#         for num in rotateArray[1:]:

#             if start_one > num:
#                 return num
#             start_one = num


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return None

        left = 0
        right = len(rotateArray) - 1

        while rotateArray[left] >= rotateArray[right]:
            
            if right - left == 1:
                return rotateArray[right]
            
            mid = (left + right)//2
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            
            if rotateArray[mid] <= rotateArray[right]:
                right = mid
        

if __name__ == "__main__":
    
    arr = [3,4,5,1,2]
    print(Solution().minNumberInRotateArray(arr))

        


