class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            stack.append(digit)
        
        res = stack[:-k] if k else stack
        res = ''.join(res).lstrip('0')
        if not res:
            return '0'
        
        return res
