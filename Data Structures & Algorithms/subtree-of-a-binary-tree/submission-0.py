# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, node1: Optional[TreeNode], node2: Optional[TreeNode])->bool:
        if node1==None and node2==None:
            return True
        elif not node1 or not node2 or node1.val!=node2.val:
            return False
        return self.isSameTree(node1.left,node2.left)and self.isSameTree(node1.right,node2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot==None:
            return True
        elif root==None and subRoot!=None:
            return False
        elif self.isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
