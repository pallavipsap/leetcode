# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1 : inorder traversal and then sort, create BST ( Brute force )

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Method 1 : Recursive inorder ( Pointers )
        # Time complexity :
        # Space complexity :

        '''
        - two breaches : neighbour adjacent ( one breach ), not adjacent ( two breaches )
        - exchange pointer if one breach
        - for two breaches, 1st breach same approach, at 2nd breach : move F to larger number, 
        - egde case : 
        - [30 60 40 50 55 35 ]
        - [5,3,9,-2147483648,2]
        - we swap only once , be it two or one breach
        - How do we know one breach ? : only two elements interchanged, so only two breaches

        Problem : 
        - incase there are more breaches, just do inorder traversal, sort it and then create BST ( BRUTE FORCE )
        - remember we start prev and curr shift once we hit null
        - we swap only once between first and last, be it two or one breach
        - do not need to return, because only global values are changed
        '''

        self.prev = None  # TreeNode() 3 by default initialised
        # print(self.prev)
        # we need first and last pointers too
        self.first = None  # TreeNode()
        self.last = None  # TreeNode()
        self.flag = False  # global variable to class Solution

        if not root: return

        self.inorder(root)
        # swap last and first
        '''
        temp = self.first.val
        self.first.val = self.last.val
        self.last.val = temp

        '''
        self.first.val, self.last.val = self.last.val, self.first.val

        # return root # this works without return too, but we must return

    def inorder(self, root):

        # base
        if root == None: return

        # logic

        self.inorder(root.left)
        print(root.val)
        # pop()
        # typical cond in checking valid BST
        if self.prev != None and self.prev.val >= root.val:  # there is a breach

            if not self.flag:  # if flag is false, this is first breach

                self.flag = True  # to make this as first breach
                self.first = self.prev  # prev ele is first  ptr # 60
                self.last = root  # curr root is last # 40
                print(self.first.val, self.last.val)
            else:  # if flag is True, second breach
                self.last = root  # breach is at prev = 55 and curr root = 35, we just assign last, no need to assign to prev

        self.prev = root  # once we hit null we start swapping here
        self.inorder(root.right)





