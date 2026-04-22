
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)

        if s_len < p_len:
            return []
        
        ord_a = ord('a')
        res = []
        s_count = [0] * 26
        p_count = [0] * 26

        for i in range(p_len):
            s_count[ord(s[i]) - ord_a] += 1
            p_count[ord(p[i]) - ord_a] += 1
        
        if s_count == p_count:
            res.append(0)
        
        for i in range(s_len - p_len):
            s_count[ord(s[i]) - ord_a] -= 1
            s_count[ord(s[i+p_len]) - ord_a] += 1

            if s_count == p_count:
                res.append(i+1)
        
        return res