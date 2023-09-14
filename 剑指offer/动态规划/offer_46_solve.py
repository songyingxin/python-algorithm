



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max_len = 0
        tmp = 0

        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i
            dic[s[j]] = j # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            max_len = max(max_len, tmp) # max(dp[j - 1], dp[j])
        return max_len

