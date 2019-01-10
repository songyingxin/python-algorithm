

""" 解决两类问题：
1. 从节点A出发，有前往节点B的路径吗
2. 从节点A出发， 前往节点B的哪条路径最短（无权重有向图）
"""

from collections import deque


graph = {}
graph['you'] = ["alice", "bob", "claire"]
graph['bob'] = ["anuj", "peggy"]
graph['claire'] = ["thom", "jonny"]
graph["anuj"] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue.append(graph[name])
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print("{} is a mango seller".format(person))
                return True
            else:
                search_queue.append(graph[person])
                searched.append(person)
    return False

if __name__ == "__main__":

    search("you")
