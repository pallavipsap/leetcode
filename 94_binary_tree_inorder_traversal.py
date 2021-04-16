# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        
        # Method 1 : Iterative approach
        
        '''
        op = []
        # stack.append(root)
        stack = []
        
        # len of stack is not empty condition is important because, once we reach leaf root.right will become null
        # so we need to see length of stack to continue the looping
        
        while root or len(stack)!=0: # 5 
            # when len of stack is 0 :
            # length of stack is 0 -- when left tree is traversed
            # but root,right is present, so while loop is executed
            
            
            
            # while root is None.. dont go to left
            print("inside")
            while root: # 4.right, 5
                stack.append(root) # 3
                root = root.left
                
            root = stack.pop() # 4, # 2, # 5, 1 , 3
            print("popped",root)
            op.append(root.val) # 4 , 2, 5, 1, 3
            print(op)
            
            # if root.right: # 5
            root = root.right # 4.right, 2.right, null
            
        return op
        
        '''
        
        # Method 2 : Recursive approach (dfs written inside the function)
        
        def dfs(root):

            if root == None:
                return

            dfs(root.left)
            op.append(root.val)
            dfs(root.right)
        
        op = []
        dfs(root)
        return op
        
    
        # Method 3 : Recursive approach (dfs written inside outside the function)
          
        
        '''
            self.op = []
            self.dfs(root)
            return self.op

        def dfs(self,root):

            if root == None:
                return

            self.dfs(root.left)
            self.op.append(root.val)
            self.dfs(root.right)


        '''
        
       
        
        
        
        
            
                
            
                
        
        
        