class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right
        else:
            return False
