# Pallavi Sapale
# June 16, 2020
# to understand inorder 
# Yet to confirm why prev = None, and not root
# Yet to try third approach ( inf )
# why prev is None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # use self.prev while using prev, this is not considered as a global variable
    # prev local to this specific class, self suggests its local to a specific class
    

    def isValidBST(self, root: TreeNode) -> bool:
        
        # Method 2 : Recursive approach :
        # does not work in leetcode when prev is global
        # Time Complexity : O(n) == we visit all nodes exactly once
        # Space Complexity : O( height of tree) == O(n) worst case
        
        # recursive does not work on leet code when prev used as global variable
        
        self.prev = TreeNode()
        self.prev = None
        return self.inOrder(root)
        

    def inOrder(self, root): # added for recursion
        
        if root == None: return True
        if self.inOrder(root.left) == False:  # if left subtree is not BST
            return False

        if self.prev != None and self.prev.val >= root.val:  # compare the values not trees
            print(self.prev.val)
            return False
        self.prev = root  # else we update prev as the root, and  ofcourse we change our root here at the bottom

        return self.inOrder(root.right)  # explore right subtree if left subtree is a BST

        # Method 1 : iterative approach : Works in leetcode -- detailed explanation
        # Time Complexity : O(n) == we visit all nodes exactly once,
        # Space Complexity : O( height of tree) -- this gives more clarity
        # if tree is one sided only ( stick ).. O(n)

        '''
        - Use in order traversal, because nodes are arranged in ascending order, which is true for a valid BST
        - set prev and root values to compare everytime
        - Remember, once you pop the node, you do not insert same node again
        Problems : 
        - while condition prev >=root ( do not forget equal to), otherwise fails for [1,1], look at th question
          node is less than or greater than, not equal to
        - do not assign prev = TreeNode(None), default value is 0
        - Figure out why prev = None
        - edge cases : [0], [1,1], []

        '''
        '''

        # pre and root values : root value is the first node, prev is null
        #prev = TreeNode()
        prev = None # Initialises prev = None/Null prev.val will not be defined initially
        #print(root,root.val)
        stack = []

        #if root == None: return True #.. This condition is taken care by while below
        while root!=None or len(stack)!=0:
            while root!=None: # keep going left until Null is hit
                stack.append(root) # pending the pointer to the tree
                root=root.left
            root = stack.pop()
            #root = stack.pop()

            # Only addition in inorder traversal---------
            # Case [1,1 ] : return False when prev = root [1,1]
            # Case [0], if prev!=None is False, because prev remains None
            #if prev!=None and prev.val >= root.val: # here we check only when prev exists and then we make sure prev>root
            if prev!=None and prev.val >= root.val: # cpmpare the values not trees
                print(prev.val)
                return False
            prev = root # else we update prev as the root, and  ofcourse we change our root here at the bottom
            #----------------------------------
            root = root.right # update root
        return True

        '''

        # Method 1.1 : other way to do iterative approach
        '''
        stack = []
        curr_val = float('-inf')
        while root or len(stack)!= 0:
            
            while root:
                stack.append(root) # append root, not val
                root=root.left
                
            # pop before going ot right
            root = stack.pop()
            if root.val <= curr_val: # [1,1] should return false, hence <=
                return False # if new value ( root value ) is less than curr value, return False
            curr_val = root.val
            root = root.right
        
        return True
        '''

        # other ways to do recursion

        # Method 2.1 :  Recursion without flag condition
        '''
        self.flag = True
        self.curr = float(-inf) # negative values also present so go for negative infinity
        self.dfs(root)
        return self.flag

        def dfs(self,root):

            if root == None:
                return

            self.dfs(root.left)
            if root.val <= self.curr: # if next value is less than curr , flag = False
                self.flag = False
            else:
                self.curr = root.val

            self.dfs(root.right)
        
        '''   
        # Method 2.3 :  Recursion with flag condition (to not call recursion further, and keep returning)
        '''
        self.flag = True
        self.curr = float(-inf) # negative values also present so go for negative infinity
        self.dfs(root)
        return self.flag

        def dfs(self,root):
            
            # recursion will keep going on, if Flas condition is not mentioned, this also gives correct output but once flag is False, further recursion calls are unnecessary
            if root == None or self.flag == False: # this does not add more recursion calls to the stack. once flag is False, irrespective of root being None, we return
                return
            
            self.dfs(root.left)
            if root.val <= self.curr: # if next value is less than curr , flag = False
                self.flag = False
            else:
                self.curr = root.val
            
            self.dfs(root.right)
        '''
       

            
        