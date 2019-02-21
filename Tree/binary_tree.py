# -*- coding:utf-8 -*-

class Node(object):
    
    def __init__(self, elem, lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
    
class Tree(object):
    