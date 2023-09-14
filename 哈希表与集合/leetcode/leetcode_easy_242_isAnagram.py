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