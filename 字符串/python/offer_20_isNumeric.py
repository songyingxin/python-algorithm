# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False
        
        hasE = False
        is_decimal = False
        has_sign = False

        for i in range(len(s)):
            # 如果有 e(E)， 只能有一个e且不能是最后一个
            if s[i] == 'e' or s[i] == 'E':
                if hasE or i == len(s) - 1:
                    return False
                hasE = True
            
            # 小数点不能重复出现或在e之后出现
            elif s[i] == '.':
                if hasE or is_decimal:
                    return False
                
                is_decimal = True
            
            elif s[i] == '-' or s[i] == '+':
                #  +- 必须在 e 的后面
                if has_sign and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                
                if not has_sign:
                    if i != 0 and s[i-1] != 'e' and s[i-1] != 'E':
                        return False
                
                has_sign = True
            elif s[i] < '0' or s[i] > '9':
                return False
            
        return True


                


        


        
        


        




    

                

    

        


        
