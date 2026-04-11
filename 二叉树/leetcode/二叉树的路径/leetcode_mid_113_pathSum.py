class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []
        def dfs(node, target, item):
            if not node:
                return
            
            target -= node.val
            item += [node.val]
            if not node.left and not node.right:
                if target == 0:
                    res.append(item)

                return
            
            dfs(node.left, target, item[:])
            dfs(node.right, target, item[:])
        
        dfs(root, targetSum, [])

        return res
