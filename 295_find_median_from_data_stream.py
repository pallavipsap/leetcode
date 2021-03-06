# March 06,2021

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = [] # x : stores all lower elem, [ 1,  3,  4]
        self.minHeap = [] # y : stores all higher elem [ 6 , 8 , 10 ]
        

    def addNum(self, num: int) -> None: 
        
        # Method 1 : just keep inserting insert(O(n)) and when asked for median, sorting(O(nlogn)) and give median at specific place(O(1))
        Time : O(n + nlogn + 1) ==O(logn)
        Space : O(1)
        
        # Method 2 : using binary search (logn) and insert(n) - since we have to shif elements
        # Time : O(logn + n) == O(n)
        # Space : O(1)
        
       
        # Method 3: use one heap, keep heaifying, when asked for median ,pop elements upto median
            
        # Method 4 : Two heaps, min and max
        # Time : O(logn) # we heapify here, just one AddNum operation takes logn and not nlogn, we are not heapifying n times
        # Space: O(n)
        
        '''
        - using two heaps ( min and max)
        - max = [ 1,  3,  4] ->top <-  min = [ 6 , 8 , 10 ]
        - duplicate values also handled
        
        '''
        
        if len(self.maxHeap) == 0: # only first insertion
            heapq.heappush(self.maxHeap,-num)
        
        elif num > -self.maxHeap[0]: # if current value > top max value in max heap, insert in min heap
            heapq.heappush(self.minHeap,num)
        else:
            heapq.heappush(self.maxHeap,-num)
        
        #print("before min",self.maxHeap)
        #print("before max",self.minHeap)
        
        minHeap_len = len(self.minHeap)
        maxHeap_len = len(self.maxHeap)
        
        # if different between both heaps exceeds 1, we have to transfer to lower length heap
        
        
        if abs(maxHeap_len - minHeap_len) > 1:
            if maxHeap_len>minHeap_len:
                val = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap,-val)
            else:
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap,-val)
        
        #print("after max",self.maxHeap)
        #print("after max",self.minHeap)
        

    def findMedian(self) -> float:
        
        minHeap_len = len(self.minHeap)
        maxHeap_len = len(self.maxHeap)
        
        if minHeap_len == maxHeap_len:
            return (self.minHeap[0]+ (-self.maxHeap[0]))/2
        elif len(self.minHeap)>len(self.maxHeap): # min heap length higher, return from min heap
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()