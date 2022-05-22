



class Solution:
    def ReverseSentence(self , str: str) -> str:
        # write code here
        return ' '.join(str.split()[::-1])