# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序遍历：根左右， 中序遍历：左根右
# 与画树的思路一致，以 pre[0] 为头节点，根据 tin 划分左，右子树范围，分别递归遍历

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        head = TreeNode(pre[0])
        head_index = tin.index(pre[0])
        head.left = self.reConstructBinaryTree(pre[1:1+head_index], tin[:head_index])
        head.right = self.reConstructBinaryTree(pre[1+head_index:], tin[1+head_index:])
        return head


if __name__ == "__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]

    print(Solution().reConstructBinaryTree(pre, tin).left.val)
