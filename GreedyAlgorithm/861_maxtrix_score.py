class Solution:
    def matrixScore(self, A):
        if not A:
            return 0
        # 先按照行翻转，如果第一个数不为1 则，翻转改行
        for vals in A:
            if vals[0] == 0:
                for i in range(len(vals)):
                    vals[i] = 1 if vals[i] == 0 else 0
        
        B = self.get_B(A)

        # 对B的每一行遍历，如果0的个数过半，则翻转该行

        for vals in B:
            cout_0 = vals.count(0)
            if cout_0 > len(vals) // 2:
                for i in range(len(vals)):
                    vals[i] = 1 if vals[i] == 0 else 0
        
        A = self.get_B(B)
        result = 0
        print(A)
        for vals in A:
            tmp = 0
            for i in range(len(vals)):
                tmp += vals[i] * 2 ** (len(vals)-i-1)
            result += tmp
        
        return result

    def get_B(self, A):
        B = []
        for i in range(len(A[0])):
            arr = []
            for j in range(len(A)):
                arr.append(A[j][i])
            B.append(arr)
        
        return B


if __name__ == "__main__":
    
    A = [[0, 1], [1, 1]]
    print(Solution().matrixScore(A))
