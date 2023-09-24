class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        end_dict = {}
        for index,val in enumerate(s):
            end_dict[val] = index
        
        res = []
        start = 0
        while start < len(s):
            end = end_dict[s[start]]
            i = start 
            while i <= end:
                if end_dict[s[i]] > end:
                    end = end_dict[s[i]]
                
                i += 1
            
            res.append(end-start+1)
            start = end + 1
        
        return res