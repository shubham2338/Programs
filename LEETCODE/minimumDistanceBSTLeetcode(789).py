# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        md=[]
        pv=987654323456789876
        def fun(root,pv):
            if root is None:return
            fun(root.left,pv)
            md.append(root.val)
            fun(root.right,pv)
        fun(root,pv)
        for i in range(len(md)-1):
            pv=min(md[i+1]-md[i],pv)
        return pv

