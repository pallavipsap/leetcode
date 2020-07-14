# Pallavi Sapale
# Floyd's algo : Tortoise and Hare

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def find_intersect(self, head):  # For method 2

        # keep both as heads ***********
        slow_curr = head
        fast_curr = head
        '''
        while slow_curr != fast_curr:
            if fast_curr == None or fast_curr.next == None: # comparing fast help to reduce iterations
                return None
            else:
                slow_curr = slow_curr.next
                fast_curr = fast_curr.next.next

        return slow_curr
        '''
        while fast_curr != None and fast_curr.next != None:  # because we move fast by 2x, so fast.next
            # print(slow_curr,fast_curr)
            slow_curr = slow_curr.next
            fast_curr = fast_curr.next.next
            if slow_curr == fast_curr:
                return slow_curr  # intersection found

        return None  # No cycle

    def detectCycle(self, head: ListNode) -> ListNode:  # return from here for answer

        # Method 1 using hashmap
        # Time complexity : O(n) go to the end of the Linked list
        # Space complexity : O(n), convert LL to hashmap
        '''
        curr = head
        hashmap = {}

        while head == None or head.next == None:
            return None

        while curr!=None:
            hashmap[curr] = curr.val
            curr = curr.next
            if curr in hashmap : # return when node already in the hashmap
                print(curr)
                return curr

        return None

        '''
        # Method 2 : Floyd's algo, better space :

        # Time complexity : O(n) go to the end of the Linked list
        # Space complexity : O(1), No extra space

        if not head or not head.next:  # that is head == None or head.next == None
            return None

        intersect = self.find_intersect(head)  # call the function "find_intersect"
        print(intersect)

        if intersect == None:  # no intersection found
            return None

        # in case intersection is found
        # find start of cycle here
        ptr1 = head
        ptr2 = intersect

        # keep moving by 1, until we meet at the head of LL
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1  # or ptr2










