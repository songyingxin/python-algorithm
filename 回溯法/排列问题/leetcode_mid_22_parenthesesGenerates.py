class Solution:
    def generateParenthesis(self, n):

        self.n = n 
        self.res = []
        def dfs(item, left_num, right_num):
            if left_num == right_num == self.n:
                self.res.append(item)
                return
            
            if left_num > self.n or right_num > self.n:
                return
            
            # 左括号的数量必须实时比右括号数量多
            if left_num < right_num:
                return
            elif left_num == right_num:
                item = item + '('
                dfs(item, left_num+1, right_num)
            else:
                dfs(item+'(', left_num+1, right_num)
                dfs(item+')', left_num, right_num+1)
        

        dfs('', 0, 0)
        return self.res






class Solution:
    def generateParenthesis(self, n):
        self.res = []
        self.n = n
    
        def dfs(item, left_num, right_num):
            if left_num == right_num == self.n:
                self.res.append(item)
                return
            
            if left_num < self.n:
                dfs(item+'(', left_num+1, right_num)
            
            if left_num > right_num:
                dfs(item + ')', left_num, right_num+1)
        
        dfs("", 0, 0)
        return self.res
        


if __name__ == "__main__":
    n = 3

    print(Solution().generateParenthesis(n))
