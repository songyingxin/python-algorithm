class Solution:
    def largestSumAfterKNegations(self, A, K):

        for i in range(K):
            A = sorted(A)
            A[0] = -A[0]
        
        return sum(A)

if __name__ == "__main__":
    
    A = [4, 2, 3]
    k = 1

    print(Solution().largestSumAfterKNegations(A, k))
