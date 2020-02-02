# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.helper(root,0)
    def helper(self,root: TreeNode, val:int):
        #Base case
        #Here base case or terminating case is at leaf node where (root.left and root.right are None)
        if not root:
            return 0
        if root.left==None and root.right==None:
            return val*10+root.val
        
        #logic case
        
        return self.helper(root.left,val*10+root.val)+ self.helper(root.right,val*10+root.val)
        
            
            
        