class Solution:
    def isValidBST(self, root):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            """
            lower: 当前节点的下界
            upper: 当前节点的上界
            """
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False

            return True

        return helper(root)

        
    


