# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(node):
            if node is None:
                return 0
   
            return 1 + max(depth(node.left), depth(node.right))
            
        depthLeft = depth(root.left)
        depthRight = depth(root.right)
     
        if abs(depthLeft - depthRight) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right) 
