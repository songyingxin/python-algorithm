# -*- coding:utf-8 -*-




# 分析： 数组中有一个数字出现的次数超过数组长度的一半，这意味着它出现的次数比其他所有数字出现次数的和还要多。
# 思路： 从头到尾遍历数组，**保存两个值**：数组中的一个数字， 次数。 当我们遍历到下一个数字时：
#   - 如果下一个数字和我们之前保存的数字相同， 则次数+1
#   - 如果下一个数字和我们之前保存的数字不同， 则次数-1
#   - 若次数为0， 则我们保存下一个数字，并把次数设为1

#   最后还需要检测 res 最终出现的次数是否大于一半

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0

        res = numbers[0]
        times = 1

        for number in numbers[1:]:
            if times == 0:
                res = number
                times = 1
            elif number == res:
                times += 1
            else:
                times -= 1

        return res if times > 0 else 0



    
