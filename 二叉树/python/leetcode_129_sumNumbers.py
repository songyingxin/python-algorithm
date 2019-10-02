
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(node, item):

            if not node:
                return

            item.append(node.val)
            if not node.left and not node.right:
                result.append(trans(item))

            item1 = item[:]
            dfs(node.left, item1)
            dfs(node.right, item)

        def trans(item):
            final = 0
            times = 0
            for val in item[::-1]:
                final += val * 10 ** times
                times += 1

            return final

        result = []
        dfs(root, [])
        print(result)

        return sum(result)
