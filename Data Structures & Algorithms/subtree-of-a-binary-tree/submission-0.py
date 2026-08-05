class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if not r1 and not r2:
            return True
        if not r1 or not r2 or r1.val != r2.val:
            return False
        return self.sameTree(r1.left, r2.left) and self.sameTree(r1.right, r2.right)