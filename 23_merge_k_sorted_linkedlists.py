# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
- merge two sorted lists : two pointers, O(larger list), create a new list
- now for linked lists, we can do the same as above and then create a new list**

Now we do not want to create a new list, just merge the two
- create dummy node, we need to start with smaller element from two lists
- we can do without dummy node also, but we have dummy node it is generic

'''
# Method 1 :merge two lists at a time
# Time : O(nk) # merge k lists with n elements ( n is basically all elements)
# Space : O(n)

# Method 2: using heaps -  put all elements in heap
# Time : O(nlogn) # with  k it will be very close, so we can consider that all n elements were inserted and heapified
# pulling and pushing is still nlogn each

# Method 3 :using heaps : we can improve log complexity
# Time : O(nlogk) # add only k elements in heap
# Space : O(k) for heaps, creating linkedlist O(n)
# so we always pop the element and put popped.next in the list, and again heapify.. at the end, insert all elements but heapify only k elements

# from heapq import heappush, heappop
# https://leetcode.com/problems/merge-k-sorted-lists/discuss/1091006/Python-Priority-queue-solution-using-heapq -- need idx

'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy_head = head = ListNode(0)
        
        min_heap = []
        for idx, l in enumerate(lists):
            if l:
                heappush(min_heap, (l.val, idx, l))
        
        print(min_heap)
        while min_heap:
            val, idx, cur = heappop(min_heap)
            head.next = cur
            head = head.next
            if cur.next:
                heappush(min_heap, (cur.next.val, idx, cur.next))
            #head.next = None
        return dummy_head.next
'''

'''
- create a tuple with three values ( list val, index, list ref)
- heapified by value
- why need idx, heapify does not work with just list val, and list ref

'''

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # Do not return ListNode() -- it will be [0] because by default class has 0 value
        if len(lists) == 0 or lists == None: # for lists = [], lists = [ [],[],[]]
            return None   # OR ListNode().next # so we do not return [] (it can be considered as empty list), we must return ListNode None

        minHeap = []
        # for list_ref in lists:
        #     # for cases with any empty list : lists = [[1,4,5],[],[2,3]]
        #     if list_ref:
        #         heapq.heappush(minHeap,(list_ref.val,list_ref))

        for idx, l in enumerate(lists):
            if l:
                #heapq.heappush(minHeap, (l.val, l))
                heapq.heappush(minHeap, (l.val, idx, l))

        # print(minHeap)

        dummy = ListNode(-1) # create a dummy
        curr = dummy

        while len(minHeap)!=0:
            # topVal, top_ref = heapq.heappop(minHeap)
            topVal,idx, top_ref = heapq.heappop(minHeap)

            # to make sure we are not inserting null elements inside heap, we confirm before puttin next element for popped value
            if top_ref.next:
                # heapq.heappush(minHeap,(top_ref.next.val, top_ref.next))
                heapq.heappush(minHeap, (top_ref.next.val,idx, top_ref.next))

            curr.next = top_ref # append top element to curr
            curr = curr.next # or top

        # print(minHeap)
        # print(dummy.next)
        return dummy.next
        
        