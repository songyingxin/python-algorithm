import collections

class Solution:
    def longestPalindrome(self, s):

        has_odd = 0
        result = 0
        for _,val in collections.Counter(s).items():
            result += val //2 * 2
            if val % 2!= 0:
                has_odd = 1
        
        return result + has_odd