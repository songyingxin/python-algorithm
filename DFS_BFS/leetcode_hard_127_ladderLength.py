
# https://leetcode-cn.com/problems/word-ladder/

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        word_set = set(wordList)

        queue = [beginWord]
        next_word = []

        depth = 1

        while queue:
            for word in queue:
                if word == endWord:
                    return depth
                
                for index in range(len(word)):
                    for indice in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:index] + indice +  word[index+1:]
                        if new_word in word_set:
                            word_set.remove(new_word)
                            next_word.append(new_word)

            depth += 1
            queue = next_word
            next_word = []
        return 0

# BFS : 常规做法
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        L = len(beginWord)

        all_com_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_com_dict[word[:i] + '*' + word[i+1:]].append(word)
        
        queue = [(beginWord, 1)]
        visited = {beginWord:True}

        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                inter_word = current_word[:i] + '*' + current_word[i+1:]
                for word in all_com_dict[inter_word]:
                    if word == endWord:
                        return level + 1
                    
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                all_com_dict[inter_word] = []
        
        return 0


# 双向 BFS


class Solution(object):

    def __init__(self):
        self.length = 0
        self.all_com_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.pop(0)

        for i in range(self.length):
            inter_word = current_word[:i] + '*' + current_word[i+1:]

            for word in self.all_com_dict[inter_word]:
                if word in others_visited:
                    return level + others_visited[word]

                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level+1))

        return None

    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.all_com_dict[word[:i] + '*' + word[i+1:]].append(word)

        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]

        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}

        ans = None

        while queue_begin and queue_end:
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans

            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0