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


# 思路：采用一个双端队列S， 存储最大值所在的下标。 
class Solution:
    def maxInWindows(self, num, size):
        # write code here

        queue = []  # 存储最大值所在下标
        res = [] # 存储最终结果
        i = 0

        while size > 0 and i < len(num):
            # 超出范围的去掉
            if len(queue) >0 and i-size+1 > queue[0]:
                queue.pop(0)
            
            # 当前值大于之前的值，之前的不可能是最大值，可以删掉
            while len(queue) > 0 and num[queue[-1]] < num[i]:
                queue.pop()
            
            queue.append(i)

            # 滑动窗口满的时候
            if i >= size - 1:
                res.append(num[queue[0]])
            i += 1
        return res


            

            
if __name__ == "__main__":
    
    nums = [2, 3, 4, 2, 6, 2, 5, 1]
    size = 3
    print(Solution().maxInWindows(nums, 3))
