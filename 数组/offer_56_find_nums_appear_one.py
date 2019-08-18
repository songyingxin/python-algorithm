# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here

        tmp = []
        for a in array:
            if a in tmp:
                tmp.remove(a)
            else:
                tmp.append(a)
        return tmp

        
if __name__ == "__main__":
    
    arr = [2, 4, 3, 6, 3, 2, 5, 5]

    Solution().FindNumsAppearOnce(arr)
