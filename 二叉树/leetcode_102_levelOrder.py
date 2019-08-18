# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]

        while queue:
            tmp = []
            next_level = []

            for i in queue:
                tmp.append(i.val)

                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            
            queue = next_level
            res.append(tmp)
        
        return res


