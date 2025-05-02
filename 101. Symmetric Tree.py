# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(leftroot,rightroot):
            if leftroot==None and rightroot==None:
                return True
            if leftroot!=None and rightroot==None or leftroot==None and rightroot!=None:
                return False
            if leftroot.val==rightroot.val:
                return isSym(leftroot.left,rightroot.right) and isSym(leftroot.right,rightroot.left)
            else:
                return False
        return isSym(root,root)
