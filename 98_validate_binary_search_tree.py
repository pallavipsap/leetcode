# June 16, 2020
# Yet to confirm why prev = None, and not root
# Yet to try third approach ( inf )

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # global variable prev
    prev = TreeNode()
    prev = None

    def isValidBST(self, root: TreeNode) -> bool:
        # Method 2 : Recursive approach :
        # does not work in leetcode when prev is global
        # Time Complexity : O(n) == we visit all nodes exactly once
        # Space Complexity : O( height of tree) == O(n) worst case
        return self.inOrder(root)

    def inOrder(self, root):

        if root == None: return True
        if self.inOrder(root.left) == False:  # if left subtree is not BST
            return False

        if prev != None and prev.val >= root.val:  # compare the values not trees
            print(prev.val)
            return False
        prev = root  # else we update prev as the root, and  ofcourse we change our root here at the bottom

        return self.inOrder(root.right)  # explore right subtree if left subtree

        # Method 1 : iterative approach : Works in leetcode
        # Time Complexity : O(n) == we visit all nodes exactly once
        # Space Complexity : O( height of tree)

        '''
        - Use in order traversal, because nodes are arranged in ascendign order, which is true for a valid BST
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
            while root!=None:
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
