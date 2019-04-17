
class TrieNode:
    def __init__(self):
        self.child = [None] * 26  # 孩子
        self.path = 0   # 记录有多少个字符串经过该路径
        self.end = 0   # 记录有多少个字符串以该节点为结尾

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word == None:
            return
        node = self.root
        for val in word:
            index = ord(val) - ord('a')
            if node.child[index] == None:
                node.child[index] = TrieNode()
            node = node.child[index]
            node.path += 1
        node.end += 1
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word == '':
            return True
        
        node = self.root
        for val in word:
            index = ord(val) - ord('a')
            if node.child[index] == None:
                return False
            node = node.child[index]
        return False if node.end == 0 else True
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node  = self.root
        for val in prefix:
            index = ord(val) - ord('a')
            if node.child[index] == None:
                return False
            node = node.child[index]
        return False if node.path == 0 else True

    def delete(self, word):
        if self.search(word) != False:
            node = self.root
            for val in word:
                index = ord(val) - ord('a')
                node.child[index].path -= 1
                if node.child[index].path == 0:
                    node.child[index] = None
                    return
                node = node.child[index]
            node.end -= 1