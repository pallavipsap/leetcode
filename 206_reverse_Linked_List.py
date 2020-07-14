# Pallavi Sapale

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # Method 1 : Iterative approach ( preferred )
        # Time : O(n)
        # Space : O(1)

        '''
        # Draw on white board

        # do not move prev = curr directly, make sure to establish connection between prev and curr

        '''

        if head == None or head.next == None:
            return head
        # prev = ListNode()
        # fast = ListNode()

        prev = None
        curr = head
        fast = curr.next

        while curr.next != None:  # or fast != None ( its the same )
            curr.next = prev
            prev = curr
            curr = fast
            fast = fast.next

        curr.next = prev
        return curr

        # Method 2 : Recursion :
        # Time : O(n) , go until end of LL
        # Space : O(n) ,  stack space

        '''

        # base case
        if head == None or head.next == None: # like iterative
            return head

        rev = ListNode()
        #recursion should terminate at 5 ( 4.next) , not at None ( null at the end )
        rev = self.reverseList(head.next) # we call head.next and not head, I want to point my rev at 5 ie. head.next

        # head = stack.pop because recusrion terminated, head keeps changing according to the stack popping

        head.next.next = head # 5 ==> head.next, I want to point 5.next back to 4 ( 4 is head which is popped from stack)
        head.next = None

        return rev

        '''



