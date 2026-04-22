class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        # 构建单调递增的栈
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            stack.append(digit)
        
        # 如果 k > 0， 则删除末尾的k个字符
        res = stack[:-k] if k else stack
        res = ''.join(res).lstrip('0')
        
        if not res:
            return '0'
        
        return res
