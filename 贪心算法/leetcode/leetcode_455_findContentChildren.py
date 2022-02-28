class Solution:
    def findContentChildren(self, g, s):
        result = 0  # 可优化，其最终等于j
        s = sorted(s)
        g = sorted(g)
        i = 0   # g 的指针
        j = 0   # s 的指针

        while(i < len(g) and j < len(s)):
            if s[j] >= g[i]:
                i += 1
                j += 1  # 可优化
                result += 1
            else:
                j += 1

        return result

if __name__ == "__main__":
    
    g = [1, 2, 3]
    s = [1, 1]

    print(Solution().findContentChildren(g,s))
            



