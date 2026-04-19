class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []  # 单调递增的栈
        res = [0] * len(temperatures)
        for index, num in enumerate(temperatures):

            # 将栈中比 num 小的数据坐标都出栈
            while stack and temperatures[stack[-1]] < num:
                pre_index = stack.pop()
                res[pre_index] = index - pre_index
            
            # 将当前的坐标入栈
            stack.append(index)
        
        return res