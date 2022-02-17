class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)

        return max(left_depth, right_depth) + 1


        