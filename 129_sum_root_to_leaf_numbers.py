# Pallavi Sapale

# Done on June 27, 2020
# We can use preorder or inorder traversal
# go through again to understand recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        # Method 2 : Recursive solution : ( Stack under the hood ) complexities same as iterative
        # Time complexity : O(n) - all nodes hit once
        # Space complexity : O( h ), best case O(log n), worst case ( O(n) -- skewed tree)
        '''
        - If we reach base case and stack is not empty, and we hit null we pop the next element and then go to right

        Problem :
        - Keep in mind, curr sum is one step back
        - tuple is taken care of, when we pass root and sum in check_sum function
        '''

        '''
        total_sum = self.check_sum(root,0)  # sum is one step back, as we pushed curr_sum as 0 along with root = 4

        return total_sum

    def check_sum(self,root,curr_sum): # local variable curr_sum

        # base case :
        if root == None : return 0 # this is function level call, coz stack is not empty == its passed to previous level in stack, 
        # stack is not empty is under the hood
        # when base case is hit, and stack is not empty we pop the element, we do not go directly to root.right
        # when we have a case where left child is not present but right child is., not needed in strict binary tree
        # take the element out of stack and then go to right


        #logic
        if root.left == None and root.right == None: # --part 2
            return curr_sum*10 + root.val # Multiply by 10 and add curr val ... 495*10 + 7

        left = self.check_sum (root.left,curr_sum*10 + root.val) # 0................part 1 
        # root = 5, curr_sum = 49, the go to left as null hit on left
        right = self.check_sum (root.right,curr_sum*10 + root.val) # ................part 3
        # when right call done, root = 7, curr_sum = 495, hit none ,, go to base case
        return left + right # to sumNumbers
        '''

        # Method 1 : Iterative solution : ( Stack over the hood )
        # Time complexity : O(n) - all nodes hit once
        # Space complexity : O( h ), best case O(log n), worst case ( O(n) -- skewed tree)

        '''
        - Concept built on in order traversal
        - put root and sum together as a tuple in the stack
        - Multiply by 10 with currsum and then insert inside the stack
        - After popping check if its the leaf node, if yes save that sum to be added to total sum
        - After popping check if its the leaf node, if no multiply sum with 10 add the next node
        - curr sum is local to the stack***

        Problem :
        - If sum is considered as global, we get wrong sum; hence curr sum is local to the stack***
        - Consider sum as local
        - Do not push anything in initial stack
        - check for both right and left for leaf

        '''

        if root == None: return 0  # base case
        tuple = ()
        total_sum = 0
        curr_sum = 0
        # stack = [ ( root, 0 )] -- DO NOT do this
        stack = []
        while root != None or len(stack) != 0:  # -----------------------------part 1
            while root != None:  # check for root.right also here
                curr_sum = curr_sum * 10 + root.val  # before pushing multiply with curr sum and add curr node
                print(curr_sum, 'curr')
                stack.append((root, curr_sum))  # push root and corresponding curr_sum, local curr sum
                root = root.left

            tuple = stack.pop()  # pop tuples
            print(tuple[1], 'popped')
            # print(tuple)

            # -----------------------------------------------addition to inorder traversal
            root = tuple[0]  # tuple (root, curr_sum)
            curr_sum = tuple[1]
            print(curr_sum)

            # check if every popped root is leaf, if yes then add to total sum
            # edge case [1-0] # here it considers 1 also as leef node as its right is null
            # But 1 actually has 0 on left, so just having None as 0, we cant say its a leaf
            if root.left == None and root.right == None:  # -----------------------part 2
                total_sum += curr_sum  # here we do not multiply the curr sum again a s in recursion
                print("total", total_sum)
            # -------------------------------------------------
            root = root.right  # if not leaf we now go to right, then go to inner while loop, check if None ----# part 3
            # print('root',root)

        print(total_sum)
        return total_sum























