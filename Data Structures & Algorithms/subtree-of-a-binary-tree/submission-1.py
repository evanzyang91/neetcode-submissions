# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def dfs(self, p, q):
        if not p and not q:
            return True
            
        if not p or not q:
            return False
            

        return p.val == q.val and self.dfs(p.left, q.left) and self.dfs(p.right, q.right)
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False
            
            if self.dfs(p, q):
                return True
            
            return isSame(p.left, q) or isSame(p.right, q)
        
        return isSame(root, subRoot)
        
            



        