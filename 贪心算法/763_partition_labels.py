class Solution:
    def partitionLabels(self, S):
        str2end = {}
        result = []
        S_len = len(S)
        for i in range(len(S)):
                str2end[S[i]] = i
        start = 0
        while( start < S_len):
            end = str2end[S[start]]
            i = start
            while  i <= end:
                if str2end[S[i]] > end:
                    end = str2end[S[i]]
                i += 1
            result.append(end - start + 1)
            start = end + 1
        return result

if __name__ == "__main__":
    
        # S = "ababcbacadefegdehijhklij"
        S = "qiejxqfnqceocmy"
        print(Solution().partitionLabels(S))
