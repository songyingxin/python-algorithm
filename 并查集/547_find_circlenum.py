

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        visit = [0 for i in range(len(M))]
        count = 0
        for i in range(len(M)):
            if visit[i] == 0:
                self.deep_find(M, i, visit)
                count += 1
        
        return count

    

    def deep_find(self, M, user,  visit):

        visit[user] = 1
        for i in range(len(M[user])):
            if visit[i] == 0 and M[user][i] == 1:
                self.deep_find(M, i, visit)

