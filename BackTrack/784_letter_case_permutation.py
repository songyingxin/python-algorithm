class Solution:
    def letterCasePermutation(self, S: str):
        
        arr = []
        index = 0
        arr.append(S)
        self.letter(S, index, arr)

        return arr

    def letter(self, S, index, arr):
        """ 回溯查找 
        arr: 存储改变后的字符串
        """
        if index >= len(S) :
            return None
        if not S[index].isdigit():
            new_str = list(S[:])
            new_str[index] = new_str[index].lower(
            ) if new_str[index].isupper() else new_str[index].upper()
            new_str = ''.join(new_str)
            arr.append(new_str)
            self.letter(new_str, index + 1, arr)

        self.letter(S, index + 1, arr)
        

if __name__ == "__main__":
    S = "a1b2"
    arr = Solution().letterCasePermutation(S)
    print(arr)
    
