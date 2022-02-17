class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if not t1 and not t2:
            return

        if t1 and t2:
            node_val = t1.val + t2.val
        elif not t1 and t2:
            node_val = t2.val
        elif t1 and not t2:
            node_val = t1.val

        node = TreeNode(node_val)

        if t1 and t2:
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
        elif not t1 and t2:
            node.left = self.mergeTrees(None, t2.left)
            node.right = self.mergeTrees(None, t2.right)

        elif t1 and not t2:
            node.left = self.mergeTrees(t1.left, None)
            node.right = self.mergeTrees(t1.right, None)

        return node


# 精简解法
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and t2:
            return t2
        elif t1 and t2:
            t1.val = t2.val+t1.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
