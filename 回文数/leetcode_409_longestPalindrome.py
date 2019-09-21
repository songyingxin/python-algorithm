import collections
class Solution:
    def longestPalindrome(self, s):

        result = 0
        for _,val in collections.Counter(s).items():
            result += val //2 * 2
            if val % 2!= 0 and result % 2 == 0:
                result += 1
        
        return result


        



