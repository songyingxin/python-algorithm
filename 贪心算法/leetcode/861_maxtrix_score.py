class Solution:
    def matrixScore(self, A):
        if not A:
            return 0

        m = len(A)
        n = len(A[0])
        # 先按照行翻转，如果第一个数不为1 则，翻转改行
        for i in range(m):
            if A[i][0] != 1:
                for j in range(n):
                    A[i][j] = 0 if A[i][j] == 1 else 1
        
        for i in range(n):
            count_0 = 0
            for j in range(m):
                if A[j][i] == 0:
                    count_0 += 1

            if count_0 > m // 2:
                for j in range(m):
                    A[j][i] = 0 if A[j][i] == 1 else 1

        # 求和
        
        return B


if __name__ == "__main__":
    
    A = [[0, 1], [1, 1]]
    print(Solution().matrixScore(A))
