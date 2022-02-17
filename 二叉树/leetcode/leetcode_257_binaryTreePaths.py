class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def dfs(node, item):
            if not node:
                return

            item.append(str(node.val))

            if not node.left and not node.right:
                item = '->'.join(item)
                result.append(item)
                return
            
            item1 = item[:]

            dfs(node.left, item1)
            dfs(node.right, item)
        
        result = []
        dfs(root,[])
        
        return result
        
