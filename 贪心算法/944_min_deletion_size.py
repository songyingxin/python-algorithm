class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        delete_arr = []
        for i in range(len(A[0])):
            for j in range(1, len(A)):
                if A[j-1][i] > A[j][i]:
                    delete_arr.append(i)
                    break
        
        return len(delete_arr)
            

