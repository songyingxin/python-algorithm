class Solution:
    def nthUglyNumber(self, n):
        help = []
        help.append(1)
        i2 = 0
        i3 = 0
        i5 = 0

        for i in range(n-1):
            help.append(min([2 * help[i2], 3 * help[i3], 5 * help[i5]]))
            if help[-1] == 2 * help[i2]:
                i2 += 1
            if help[-1] == 3 * help[i3]:
                i3 += 1
            if help[-1] == 5 * help[i5]:
                i5 += 1
        
        return help[-1]


class Solution:
    def isUgly(self, num):
        if num == 0:
            return False
        while num % 2 == 0:
            num = num / 2
        while num % 3 == 0:
            num = num / 3
        while num % 5 == 0:
            num = num / 5
        return True if num == 1 else False



n = 10

print(Solution().nthUglyNumber(n))
            
