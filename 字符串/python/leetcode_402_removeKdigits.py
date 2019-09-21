class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if len(num) == k:
            return '0'
        
        if k == 0:
            return num
        
        stack = []
        res = ''

        end_point = -1

        for index, val in enumerate(num):

            if len(stack) == 0 or int(val) >= int(stack[-1]):
                stack.append(val)
            
            else:
                while len(stack) > 0 and int(val) < int(stack[-1]):
                    stack.pop()
                    k -= 1
                    if k == 0:
                        break
                
                stack.append(val)
            
            if k == 0:
                end_point = index
                break
        
        if k == 0:
            res = ''.join(stack) + num[end_point + 1:]
        
        else:
            while k != 0:
                stack.pop()
                k -= 1
            
            res = ''.join(stack)
        
        return str(int(res))

