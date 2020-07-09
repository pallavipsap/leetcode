# Definition for a binary tree node.
# to understand backtracking
# yet to try with iterative approach and DFS
# similar to 129. root to leaf
# does not work


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # global variables
    global target
    # global result
    global result
    result = []
    target = 0

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        # Method 2 : Recursive solution : ( Stack under the hood ) complexities same as iterative
        # Time complexity : O(n) - all nodes hit once
        # Space complexity : O( h ), best case O(log n), worst case ( O(n) -- skewed tree)

        # Method 1 : Iterative solution : ( Stack over the hood )
        # Time complexity : O(n) - all nodes hit once
        # Space complexity : O( h ), best case O(log n), worst case ( O(n) -- skewed tree)

        '''
        Problem :
        - remember it is root to leaf node

        '''

        result = []  # stores paths in lists of lists
        target = 0
        target = sum
        newpath = []
        result = self.check_sum(root, 0, [], sum)
        return result  # no need to return here

    def check_sum(self, root, curr_sum, path, sum):

        # base case:
        if root == None: return  # should be return 0, but

        # logic

        # before checking for leaf , lag in stack is fixed
        curr_sum += root.val  # root = 5, curr_Sum = 5, root = 4, curr_sum = 9
        path.append(root.val)
        # check leaf
        if root.left == None and root.right == None:
            if sum == curr_sum:  # made target a global variable
                print(target)
                newpath = path
                result.append(path)  # we are adding the same path ( pointer to path again and again)
                path = []
                print(result)

        self.check_sum(root.left, curr_sum, path.copy(),
                       sum)  # done in slightly different manner than leet problem : 129
        self.check_sum(root.right, curr_sum, path.copy(), sum)

        # uncomment this to see the results
        # self.check_sum(root.left,curr_sum,path,sum) # done in slightly different manner than leet problem : 129
        # self.check_sum(root.right,curr_sum,path,sum)

        return result





















