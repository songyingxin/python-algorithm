class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.lookup
        for val in word:
            if val not in tree:
                tree[val] = {}
            tree = tree[val]
        
        tree['#'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def dfs(word, tree):
            if not word:
                if '#' in tree:
                    return True
                return False
            
            if word[0] == '.':
                for val in tree:
                    if dfs(word[1:], tree[val]):
                        return True
            elif word[0] in tree:
                if dfs(word[1:], tree[word[0]]):
                    return True
            
            return False
        
        return dfs(word, self.lookup)

