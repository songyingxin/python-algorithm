class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        end_dict = {}
        for i,val in enumerate(s):
            end_dict[val] = i
        
        res = []
        left = 0
        right = 0

        for i,val in enumerate(s):
            right = max(right, end_dict[val])

            if i == right:
                res.append(right-left+1)
                left = i+1
        
        return res