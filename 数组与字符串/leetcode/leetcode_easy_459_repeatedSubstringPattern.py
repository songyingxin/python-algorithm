class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
      new_s = s+s 
      new_s = new_s[1:-1]
      return s in new_s