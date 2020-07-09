# Pallavi Sapale
# June 3, 2020
# Try 2nd method

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # Method 1 : Slow solution
        # Time Complexity : O(n^2)
        # Because O(n) ( 4 arrays ) at every node ( at n nodes)
        # Space Complexity : O (n) for n tree nodes

        '''
        - preorder : Root L R, inorder : L Root R
        - First understand why only inorder and preorder cannot be used to create trees
        - draw both inorder and preorder, iterate through preorder to find the root

        Problem :
        - do not forget to right self while calling the function
        - check the edge case
        - Time complexity is O(N^2)
        - even if u use indexof** indexAt**
        '''

        # edge case
        if len(preorder) == 0 or len(
                inorder) == 0:  # doing either of the two is also okay, because if even one is [], o/p in None
            return None

        root = TreeNode(preorder[0])

        # iterate over inorder and find that root
        # iterating over inorder traversal again and again to find the root
        for i in range(len(inorder)):  # even if u use indexof** indexAt**
            if inorder[i] == root.val:
                index = i  # index of root in the inorder list

        # create 4 arrays to split two arrays
        # last element in the list given below is not included
        preLeft = preorder[1:index + 1]  # will go upto index
        preRight = preorder[index + 1:len(preorder)]
        inLeft = inorder[0:index]  # do not consider root
        inRight = inorder[index + 1: len(inorder)]

        # print(preLeft)
        # print(preRight)

        # recursive calls, because we need both pre left and pre Right to
        root.left = self.buildTree(preLeft, inLeft)
        root.right = self.buildTree(preRight, inRight)
        # print(root)
        return root

