class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        stack, r = [], [0] * len(T)

        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                 r[stack.pop()] = i - stack[-1]
            
            stack.append(i)
        return r


