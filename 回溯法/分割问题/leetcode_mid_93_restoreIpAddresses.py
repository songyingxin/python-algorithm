class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        n = len(s)

        def dfs(item, start_index):
            if len(item) == 4:
                if start_index == n:
                    res.append('.'.join(item))
                return 

            if len(item) > 4:
                return 
            
            for i in range(start_index+1, n+1):
                sub_str = s[start_index:i]

                if 0<int(sub_str)<=255 and s[start_index] != '0':
                    dfs(item+[sub_str], i)

                if sub_str == '0':
                    dfs(item+[sub_str], i)
            
        dfs([], 0)
        return res

        




class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        

        res = []

        def dfs(item, s):
            if not s and len(item) == 4:
                item = '.'.join(item)
                res.append(item)
                return 
            
            if len(item) > 4:
                return 
            
            for i in range(1, len(s)+1):
                if (0<int(s[:i])<=255 and s[0] != '0'):
                    dfs(item+[s[:i]], s[i:])
                
                if s[:i] == "0":
                    dfs(item+[s[:i]], s[i:])
            
        dfs([], s)
        return res