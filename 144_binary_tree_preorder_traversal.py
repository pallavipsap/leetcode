# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # passing op by reference
        
        op = []
        #op.append(self.dfs(root))
        self.dfs(root,op)
        print(op)
        return op
    
    def dfs(self,root,op):
        
        if root == None:
            return
        
        op.append(root.val)
        print(op)
        self.dfs(root.left,op)
        self.dfs(root.right,op)
        # return root.val
        