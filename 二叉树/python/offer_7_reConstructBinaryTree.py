# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        # 注意pre 与 tin 的划分，左子树一直在右子树前面
        flag = TreeNode(pre[0])
        judge = tin.index(pre[0])
        flag.left = self.reConstructBinaryTree(
            pre[1:judge+1], tin[:judge])
        flag.right = self.reConstructBinaryTree(
            pre[judge+1:], tin[judge+1:])
        return flag


if __name__ == "__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]

    print(Solution().reConstructBinaryTree(pre, tin).left.val)
