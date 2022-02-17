# -*- coding:utf-8 -*-
# class Solution:
#     def maxInWindows(self, num, size):
#         # write code here

#         if size <= 0:
#             return []
        
#         res = []

#         for i in range(0, len(num) - size + 1):
#             res.append(max(num[i:i+size]))
        
#         return res

class Solution:
    def maxInWindows(self, num, size):
        # write code here

        queue = []  # 存储最大值所在下标
        res = [] # 存储最终结果
        i = 0

        if size <= 0:
            return res
        
        for i in range(len(num)):
            # 若最大值 queue[0]位置过期，则弹出
            if queue and i-size+1 > queue[0]:
                queue.pop(0)
            
            # 弹出 queue 所有比 num[i] 小的数字
            while queue and num[queue[-1]] < num[i]:
                queue.pop()
            
            queue.append(i)

            if i >= size -1:
                res.append(num[queue[0]])
            
            i += 1
        
        return res
            


            

            
if __name__ == "__main__":
    
    nums = [2, 3, 4, 2, 6, 2, 5, 1]
    size = 3
    print(Solution().maxInWindows(nums, 3))
