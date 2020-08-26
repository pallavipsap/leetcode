# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if head == None or head.next == None or k == 1:
            return head

        dummy = ListNode()
        begin = ListNode()
        i = 0
        # no need to declare end
        dummy.next = head  # start this connection because eventually we need to return dummy.next
        begin = dummy

        while head != None:
            i += 1
            if i % k == 0:  # if modulo == 0: reverse the linkedlist
                # call reverse linkedlist
                # give two nodes between which reverse should take place
                # head.next is the end node
                begin = self.reverseLinkedList(begin, head.next)
                head = begin.next  # why?
            else:
                head = head.next
        return dummy.next

    def reverseLinkedList(self, begin, end):

        prev = begin

        curr = begin.next  # curr = head
        fast = begin.next.next  # fast = head.next
        first = curr  # to connect 1 and 4

        while fast != end:  # fast!= None:
            curr.next = prev
            prev = curr
            curr = fast
            fast = fast.next

        curr.next = prev  # linkedlist reversed
        print('curr', curr)

        # establish connections
        first.next = end  # fast
        begin.next = curr  # to set begin position for next iteration
        return first  # why?







