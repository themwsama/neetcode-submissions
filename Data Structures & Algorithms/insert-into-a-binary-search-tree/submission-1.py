# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head = previous = root
        direction = None

        while root:
            rootValue = root.val
            if val > rootValue:
                previous = root
                root = root.right
                direction = "RIGHT"
            else:
                previous = root
                root = root.left
                direction = "LEFT"
        
        if direction == "RIGHT":
            previous.right = TreeNode(val=val)
        elif direction == "LEFT":
            previous.left = TreeNode(val=val)
        else:
            head = TreeNode(val=val)

        return head