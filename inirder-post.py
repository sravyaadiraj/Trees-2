# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        root_index=inorder.index(postorder[-1])
        node= TreeNode(postorder[-1])
         #logic case
        node.left=self.buildTree(inorder[:root_index],postorder[:root_index])
        print(node.left)
        node.right=self.buildTree(inorder[root_index+1:len(inorder)],postorder[root_index:-1])
        return node
        
        
       
        