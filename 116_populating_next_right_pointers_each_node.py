# done on July 24

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Method 3 : DFS appraoch, yet to be tried

from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # Method 2: Iterative solution ( pointers no queues)
        # Time complexity : O(n), all nodes
        # Space complexity : O(1) == save space
        # we are using pointers, not queue explicity. the queue itself is

        '''
        - make connections at lower level by staying one level above********
        - two conditions imp:
        - curr.left.next = curr.right : for same node with children
        - curr.right.next = curr.next.left : for different nodes with different children

        Problem :
        - its a prefect binary tree

        '''

        if root == None: return None  # if not root
        level = Node()
        level = root

        # check for level.left and not level
        # because we are staying at higher level and changing values of lower level, hence we should
        # check if a level below ( i.e. level.left) is present in which connections should be made
        while level.left != None:  # to track depth of tree
            curr = level
            while curr != None:  # to track end of a level;  do not check for curr.next!=None:, we are already doing curr.next at the bottom
                curr.left.next = curr.right
                if curr.next != None:  # now check for the next curr ( adjacent node in queue)
                    curr.right.next = curr.next.left
                curr = curr.next  # check if this is not None in while loop above
            level = level.left  # go to next level ;

        return root  # we keep changing levels, root pts is at the same place always

        # Method 1 : Iterative solution ( using queue explicitly)
        # Time complexity : O(n)
        # Space complexity : O(n)
        # last level will have n/2 leaves in complete binary tree

        '''
        - make connections at lower level by staying one level above********
        '''
        '''
         if root == None : return None # if not root
        queue = deque([root]) # add root to the queue

        while queue:

            size = len(queue)
            for i in range(size):
                curr = queue.popleft() # remove first inserted element
                if i !=size-1: # last index will be size - 1
                    nextNode = queue[0] # just append it to the top of stack
                    curr.next = nextNode # make connection between popped node and node in queue( queue[0])

                if curr.left!=None: # if left is not none, means it has right and left both
                    queue.append(curr.left) # its a prefect binary tree so both right and left are present, if left is absent right is surely absent, vice versa
                    queue.append(curr.right)

        return root

        '''








