class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return
        
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            # 叶子结点，直接删除即可
            if not root.left and not root.right:
                return None
            # 左子树为空，直接返回右子树
            elif not root.left:
                return root.right
            # 右子树为空，直接返回左子树
            elif not root.right:
                return root.left
            # 左子树，右子树均不为空
            else:
                # 找只比key大一点的节点
                node = root.right
                while node.left:
                    node = node.left

                # 调整该节点的左右节点位置
                node.right = self.deleteNode(root.right, node.val)
                node.left = root.left
                return node

        return root   