class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort(reverse=True)
        s.sort(reverse=True)

        g_index = 0
        s_index = 0
        
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                s_index += 1
                g_index += 1
            else:
                g_index += 1
        
        return s_index
            



