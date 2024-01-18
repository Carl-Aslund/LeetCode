class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return isMirror(node1.left, node2.right) and isMirror(node2.left, node1.right)
        return isMirror(root.left, root.right)