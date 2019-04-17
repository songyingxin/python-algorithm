class Solution:
    def minAddToMakeValid(self, S) :

        left = 0
        right = 0
        result = 0
        pairs = 0
        for char in S:
            if char == '(':
                left += 1
            
            if char == ')':
                right += 1

                if left != 0:
                    pairs += 1
                    left -= 1

        return len(S) - 2 * pairs

if __name__ == "__main__":
    
    S = "()))(("
    print(Solution().minAddToMakeValid(S))
