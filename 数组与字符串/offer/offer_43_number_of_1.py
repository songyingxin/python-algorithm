# -*- coding:utf-8 -*-


#  思路：对于1， 11， 21，这部分数来看，每10个数，个位上的 1 就会出现一次， 同理，每100个数， 10位上的 1 就会出现一次。 
#  对于11， 12， 13这部分数来看，如果十位上的数是 1 ，那么最后 1 的个数为 x+1， x 为个位的数值； 如果十位上的数大于 1 ，那么最后 1 的数量加 10
# 算法：将 i 从1 遍历到 n ，每次遍历 i 扩大 10倍：
# $\frac{n}{i * 10} * i$ 表示 `(i * 10)` 位上 `1` 的个数，注意，此处的分数为整除，因此不能直接约
# `min(max(n%(i*10)−i+1,0),i)` 表示需要额外数的 `(i * 10)` 位上 `1` 的个数
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here

        res = 0
        tmp = n
        base = 1
        
        while tmp:
            last = tmp % 10
            tmp = tmp / 10

            res += tmp * base
            if last == 1:
                res += n % base + 1
            elif last > 1:
                res += base
            
            base *= 10
        
        return res
