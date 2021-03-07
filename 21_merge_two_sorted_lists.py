# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Method 2 : Deal with only linkedLists
# Time : O( larger list) O(n)
# Space : O(1), if no new list is created, else O(n) for new list

# Method 1: Create array out of linkedlists, then merge two arrays and then create LinkedLists ( long process)
# Time: O(n)
# Space : O(n)



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        # without dummy
        
        '''
        if l1.val<l2.val:  # start with lower value
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        curr = head
            
        # while l1!= None and l2!=None: # keep appending until you reach null ( works )
        
        while l1 and l2:
            if l1.val<l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        print(head)
        
        if l2:
            curr.next = l2
        else:
            curr.next = l1
            
        return head
        
        '''
        
        dummy = ListNode(-1)
        
        if l1.val<l2.val:
            dummy.next = l1
            l1 = l1.next # this also takes care of single node in l1, because in while we anyways check for l1 and l2 eg. l1 = [1] l2 = [ 3,4,5]
        else:
            dummy.next = l2
            l2 = l2.next
        
        curr = dummy.next # set curr which will keep moving in while below to lower element, dummy ( which acts like head reamins there )
        
        while l1 and l2:
            if l1.val<l2.val: # l1 is smaller
                curr.next = l1
                l1 = l1.next # move l1
            else:
                curr.next = l2
                l2 = l2.next
                
            curr = curr.next # update curr to check further
        # if l1:
        #     curr.next = l1
        # else:
        #     curr.next = l2
            
        curr.next = l1 if l1 else l2
        
        return dummy.next
                
                
            
        