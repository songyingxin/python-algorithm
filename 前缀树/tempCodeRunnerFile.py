class TrieNode:
    def __init__(self):
        self.child = [None] * 27  # 孩子
        self.end = 0   # 记录有多少个字符串以该节点为结尾

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for val in word:
            if val == '.':
                index = 0
            else:
                index = ord(val) - ord('a') + 1
            
            if node.child[index] == None:
                node.child[index] = TrieNode()
            node = node.child[index]
        node.end += 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.search_word(self.root, word, self.root.end)

    
    def search_word(self, node, word, is_end):
        if len(word) == 0:
            if is_end != 0:
                return True
            return False
        
        if word[0] == '.':
            for i in range(27):
                if node.child[i] != None and self.search_word(node.child[i], word[1:], node.end):
                    return True
        else:
            index = ord(word[0]) - ord('a') + 1
            if (node.child[index] and self.search_word(node.child[index], word[1:], node.end)) or  (node.child[0] and self.search_word(node.child[0], word[1:], node.end))
                return True
        return False