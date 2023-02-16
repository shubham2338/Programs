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
        