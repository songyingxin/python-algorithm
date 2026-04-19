class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s2pattern = {}
        pattern2s = {}
        s = s.split()

        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            if s[i] in s2pattern:
                if s2pattern[s[i]] != pattern[i]:
                    return False
            else:
                s2pattern[s[i]] = pattern[i]
            
            if pattern[i] in pattern2s:
                if pattern2s[pattern[i]] != s[i]:
                    return False
            else:
                pattern2s[pattern[i]] = s[i]

        return True