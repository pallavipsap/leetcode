# Pallavi Sapale

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        '''
        - without dummy node

        if head == None: # []
            return head

        if head.next == None and n==1: # [1] n=1
            return head.next

        '''

        # Method 2 : One pass
        # Time complexity : O(n)
        # Space complexity : O(1)

        '''
        - logic is a bit tricky, use of slow and fast pointer
        - start slow and fast at the same place
        - go upto n+1 th node then start moving slow until fast reaches end of the LL
        - we do this to maintain difference between fast and slow pointers as n

        Problem :
        - fast should be at n+1 th position when we move slow, and not nth position

        '''

        # once fast is at n+1, while loop breaks now move slow and fast both
        # if fast is at nth position, then after moving slow and fast, slow will reach at the poition of node which is to be removed
        # hence fast should be at n+1th position

        dummy = ListNode(0)  # we do not care about the value in dummy node, it can be ()

        # start slow and fast at dummy
        slow = dummy
        fast = dummy
        dummy.next = head  # build connection between dummy and head

        count = 0

        while count <= n:
            count += 1
            fast = fast.next

        while fast != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

        # Method 1 : Two pass
        # Time complexity : O(n)
        # Space complexity : O(1)
        '''
        - calculate length of the linkedlist
        - LENGTH - n = x
        - then we go "upto xth" node and then delete node after that delete node after that

        Problem :
        - do not make mistake of removing xth node, node after that should be removed

        '''

        # Method 1 : Two pass
        # Time complexity : O(n)
        # Space complexity : O(1)
        '''
        - calculate length of the linkedlist
        - LENGTH - n = x
        - then we go "upto xth" node and then delete node after that delete node after that

        Problem :
        - do not make mistake of removing xth node, node after that should be removed

        '''
        '''
        dummy = ListNode(0)
        # start slow and fast at dummy
        slow = dummy
        fast = dummy
        dummy.next = head #build connection between dummy and head

        length = 0
        while fast.next!=None:
            length+=1
            fast=fast.next
        print(length)

        #if length == 1:
        #    return dummy.next.next

        remove_position = length - n # this node's next node has to be removed

        count = 0
        while count<remove_position:
            count+=1
            slow=slow.next # runs remove_position times

        #slow.next is to be removed
        slow.next = slow.next.next

        return dummy.next

        '''