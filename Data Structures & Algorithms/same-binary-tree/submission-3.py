# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            if not node1 and not node2:
                continue
            elif node1 and node2 and node1.val == node2.val:
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
            else:
                return False
        return True
            