

# 思路： dfs
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        def DFS(u, graph, visit):
            visit[u] = 1
            for i in range(len(graph[u])):
                if visit[i] == 0 and graph[u][i] == 1:
                    DFS(i, graph, visit)

        visit = [0] * len(M)
        result = 0

        for i in range(len(M)):
            if visit[i] == 0:
                DFS(i, M, visit)
                result += 1
        
        return result




class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        n = len(M)
        p = {[i] for i in range(n)} # 并查集初始化

        ans = n
        for i in range(n):
            for j in range(i, n):
                # 并查集合并
                if M[i][j] == 1 and p[i] is not p[j]:
                    p[i] += p[j]
                    for k in p[j]:
                        p[k] = p[i]
                    
                    ans -= 1
        
        return ans


