# Aug 25, 2020
# Do not return anything

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Method 1 :
        # start slow and fast pointer at same location
        '''
        Problem:
        - think about AND OR condition
        - think about both even and odd list
        - Choose wisely fast/fast.next, second/second.next to not lose any iteration

        '''
        '''
        if head == None or head.next == None: return

        first = head
        second = ListNode()
        slow = head
        fast = slow # change - same location

        '''
        slow = head
        fast = head

        '''

        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

        print(slow)
        second = self.reverseList(slow.next)


        # make end of first list as None
        slow.next = None # for even and odd list
        #print(head)

        # if we do first.next --> we will get none.none, this is the breaking condition
        # if we give an or condition below, it will keep going inside while until both become Null
        # the above condition is not possible for two list with different length, hence having an and condition is needed

        # do not do first.next!=None and second.next!=None, you will lose one interation altogether
        while second!=None and first!=None: 
            temp1 = first.next
            temp2 = second.next # None

            first.next = second # 1 5 2 4
            second.next = temp1 # 1 5 2 4 3

            first = temp1
            second = temp2 # None

        #print(head)


    def reverseList(self,curr):

        #print('in funct', curr)
        # we send None here for [1,2]
        # Need this case in Method 1 as we send None here ( slow.next == None)
        # In method 2 we do not send None
        if curr == None: return curr

        next_curr = curr.next
        prev = None

        while next_curr!=None:
            curr.next = prev
            prev = curr
            curr = next_curr
            next_curr = next_curr.next

        curr.next = prev
        return curr


        '''

        # Method 2
        # Slow and fast pointer at head

        if head == None or head.next == None: return

        first = head
        second = ListNode()
        slow = head
        fast = head.next  # change -  next location

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # print(slow)
        second = self.reverseList(slow.next)

        # make end of first list as None
        slow.next = None  # for even and odd list
        # print(head)

        # if we do first.next --> we will get none.none, this is the breaking condition
        # if we give an or condition below, it will keep going inside while until both become Null
        # the above condition is not possible for two list with different length, hence having an and condition is needed

        # do not do first.next!=None and second.next!=None, you will lose one interation altogether
        while second != None and first != None:
            temp1 = first.next
            temp2 = second.next  # None

            first.next = second  # 1 5 2 4
            second.next = temp1  # 1 5 2 4 3

            first = temp1
            second = temp2  # None

        # print(head)

    def reverseList(self, curr):

        # print('in funct', curr)

        # we send None here for [1,2]
        # if curr == None: return curr # we do not need this condition in "Method 1" as we do not send None here

        next_curr = curr.next
        prev = None

        while next_curr != None:
            curr.next = prev
            prev = curr
            curr = next_curr
            next_curr = next_curr.next

        curr.next = prev
        return curr

