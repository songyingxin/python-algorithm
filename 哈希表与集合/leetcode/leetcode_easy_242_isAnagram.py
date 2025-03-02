class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        nums = [0] * 26

        for val in s:
            nums[ord(val) - ord('a')] += 1
        
        for val in t:
            nums[ord(val) - ord('a')] -= 1
        
        for val in nums:
            if val != 0:
                return False
        
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}

        for val in s:
            if val not in s_dict:
                s_dict[val] = 1
            else:
                s_dict[val] += 1
        
        for val in t:
            if val not in s_dict:
                return False
            s_dict[val] -= 1
        
        for key,val in s_dict.items():
            if val != 0:
                return False
        
        return True
