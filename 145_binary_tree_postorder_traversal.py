# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # op = [] # for entire class, self.op is this variable only (global)
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
    
        # op = []
        self.op = [] # for entire class, self.op is this variable only (global to other functions, but local to classes)
        
        # self.op = [] # because same object is called ( leet code specific)
        # Solution.op = []
        
        self.dfs(root) # do not pass self, call usign self, which suggests its we have passed using an object
       
        # return op
        return self.op
        # return Solution.op # using op = [] in class Solution, its a class variable
       
        
    def dfs(self,root):
        
        # global op # for using global op in class
        if root == None:
            return
        
        self.dfs(root.left)
        self.dfs(root.right)
        
        # op.append(root.val)
        self.op.append(root.val)
        # Solution.op.append(root.val) #  may be creates a new op object everytime
        
        
        
        '''
        ways to use op : 
        
        1. pass op in dfs function, do not use self.op
        2. use self.op ( if dfs function is outside postorderTraversal but inside class Solution)
        3. if op is defined in class op = [], self.op can be used to access this variable
        4. if op is defined in class op = [], op as class variables, use Solution.op , not self.op
     
        
        '''
        
        
        