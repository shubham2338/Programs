# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fun(root):
            if root is None:
                return None
            temp=root.left
            root.left=rootA.right
            root.right=temp
            fun(root.left)
            fun(root.right)
            return root
        root=fun(root)
        return root