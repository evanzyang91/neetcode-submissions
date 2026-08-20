# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            curr, low, high = queue.popleft()

            if curr.val <= low or curr.val >= high:
                return False

            if curr.left:
                queue.append((curr.left, low, curr.val))
            
            if curr.right:
                queue.append((curr.right, curr.val, high))

        return True