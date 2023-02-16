# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if root is None:
                return 0
            l=depth(root.left)+1
            r=depth(root.right)+1
            if l>r:
                return l
            return r
        return depth(root)
        