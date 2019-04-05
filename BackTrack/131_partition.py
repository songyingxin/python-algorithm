class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, len_s = [], len(s)

        def dfs(re, index):
            if index == len_s:
                res.append(re)
            for i in range(1, len_s-index+1):
                hel = s[index:index+i]
                if hel == hel[::-1]:
                    dfs(re+[hel], index+i)
        dfs([], 0)
        return res


if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))
