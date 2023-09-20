class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)
        for index, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                pre_index = stack.pop()
                res[pre_index] = index - pre_index
            
            stack.append(index)
        
        return res