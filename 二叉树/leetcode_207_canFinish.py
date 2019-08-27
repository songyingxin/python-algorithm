from collections import defaultdict, deque


# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        visited = set()

        for x,y in prerequisites:
            graph[y].append(x)
        

        def dfs(i, being_visited):
            if i in being_visited:
                return False
            
            if i in visited:
                return True
            
            visited.add(i)
            being_visited.add(i)

            for j in graph[i]:
                if not dfs(j, being_visited):
                    return False
            
            being_visited.remove(i)
            return True
        
        for i in range(numCourses):
            if i in visited:
                continue
            if not dfs(i, set()):
                return False
        
        return True
            

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        degree = [0] * numCourses

        for x,y in prerequisites:
            graph[y].append(x)
            degree[x] += 1
        
        queue = deque([i for i in range(numCourses) if degree[i] == 0])
        cnt = 0
        while queue:
            i = queue.pop()
            cnt += 1
            for j in graph[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    queue.appendleft(j)
        return cnt == numCourses
