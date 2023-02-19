# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        ans=[]
        if root==None: return ans
        q.append(root)
        c=0
        while q:
            l=len(q)
            h=[]
            for i in range(l):
                s=q.pop(0)
                if s.left!=None:q.append(s.left)
                if s.right!=None: q.append(s.right)
                h.append(s.val)
            if c%2==0:
                ans.append(h)
            else:
                ans.append(h[::-1])
            c+=1
        return ans
                