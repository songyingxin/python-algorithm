class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            s_sort = tuple(sorted(s))
            if s_sort in res:
                res[s_sort].append(s)
            else:
                res[s_sort] = [s]
        return res.values()

        
# 思路2
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
