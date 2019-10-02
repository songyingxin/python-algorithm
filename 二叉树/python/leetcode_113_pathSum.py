class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        def dfs(node, sum_val, item):
            if not node:
                return

            if not node.left and not node.right and sum_val-node.val == 0:
                item += [node.val]
                result.append(item)
                return
                
            dfs(node.left, sum_val - node.val, item + [node.val])
            dfs(node.right, sum_val - node.val, item + [node.val])

        result = []
        dfs(root, sum, [])
        return result
