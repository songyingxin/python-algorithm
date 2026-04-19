class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        degree = [0] * numCourses  # 是否有依赖

        for x,y in prerequisites:
            graph[y].append(x)
            degree[x] += 1
        
        # 初始化入度为0的队列
        queue = [val for val in range(numCourses) if degree[val] == 0]
        cnt = 0
        while queue:
            val = queue.pop(0)
            cnt += 1
            for j in graph[val]:
                degree[j] -= 1
                if degree[j] == 0:
                    queue.append(j)
        return cnt == numCourses