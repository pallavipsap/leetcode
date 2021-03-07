class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        # Method 1:
        # Time : sorting(logn) + traversing(n) == O(n)
        
        '''
        sort the list in decending order, and travel to kth position from the start

        '''
        
        # Method 2 :
        
        # Using heaps: 
        # Time : nlogn
        # Space : O(n)
        '''
        - push all elements in maxheap and then keep popping k times, eventually kth element largest, kth pull is kth largest
        OR
        - push all elements in mineheap and keep popping times, eventually top element in heap is kth maximum
        
        # one line code
        # time is still nlogn
        # returns set of k largest elements in descending order, so last element is my kth largest element
        
        return heapq.nlargest(k,nums)[-1]

        '''
        
        # Method 3:
        # Time : O(nlogk)
        # Space : O(k)
        
        
        # push only k elements, follow the procedue below, we still use min heap here, and then push all elements
        # here max heap wont work, because 5 gets popped out, look at the notes
        
        # we are tryting to collect top k largest elements, create minheap, return top
        # logic is to create a minheap of k largest elements and return the top element 
        # that is return the kth largest element among k elements ( smallest element among k elements )
        # so my kth lrgest element will be 1st element in result array ( minheap ) of k elements
        # Time complexity : n log k
        
        
        # incase I am asked kth smallest element, I can just create a minheap of k elements
        # elif condition will be 
        # elif result[0] > num :   # I replace if I encounter a smaller element
        #     heapq.heapreplace(result,num)   # reult will have k sorted elements
        # return result[len(result)-1] # return last element among k elements in result array
        
        
        minHeap = []
        
        for val in nums:
            if len(minHeap)<k: # minHeap can still hold upto k elements
                heapq.heappush(minHeap,val) # minheap property is restored ie. top element is smallest in minHeap
            elif val>minHeap[0]: # swap the smallest element in the minheap (1s) with current element, if smallest element is less than current element  (num) 
                heapq.heappop(minHeap) 
                heapq.heappush(minHeap,val)
        
        return minHeap[0]
    
      
