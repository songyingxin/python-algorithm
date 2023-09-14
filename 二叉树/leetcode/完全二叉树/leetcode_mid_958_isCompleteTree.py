# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        has_empty = False
        queue = [root]

        while queue:

            node = queue[0]
            queue = queue[1:]

            if not node:
                has_empty = True
            else:
                if has_empty:
                    return False
                
                queue.append(node.left)
                queue.append(node.right)
        
        return True