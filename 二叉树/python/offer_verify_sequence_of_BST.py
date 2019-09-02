# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here

        if not sequence:
            return False
        
        root = sequence[-1]  # 左，右，根，根节点为最后一个元素

        # 在二叉搜索树中左子树节点的值小于根节点的值
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        # 二叉搜索树种右子树节点值大于根节点的值
        for j in range(i, len(sequence)):
            if sequence[j] < root:
                return False
        
        left_tree = sequence[:i]  # 左子树
        right_tree = sequence[i:-1]  # 右子树

        left_is = True
        right_is = True

        if left_tree:
            left_is = self.VerifySquenceOfBST(left_tree)
        if right_tree:
            right_is = self.VerifySquenceOfBST(right_tree)
        
        return left_is and right_is



