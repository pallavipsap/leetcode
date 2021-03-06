# Done on July 20
# Here k is not given***

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # Method 2 :
        # Time complexity : O(nlogn)  == heapify  n times , log1 + log2 + log3...logn
        # ( as we are sorting 1st ) and even in heaps if every meeting needs a different room n log n for heaps
        # Space complexity : 
        # in place sorting ( no space ), but heaps so O(n), it can be k, but every meeting can need a different space
        '''
        edge cases
        [ 0 30, 5 32, 15 20, 6 16]
        
        '''
        
        # after 1st method think about prority queues ( for that room list ) == > because we want to compare with minimum element in the room list, Hence heapes
        '''
        - we can think about value between start and end time and all, but eventually 
        We are bothered about end time of previous meeting and start time of next meeting********
        - insert end time in the heap, because it is what we are comparing our next starting time with
        - so now we know, we have to compare start time with the end time
        - so we keep pushing when curr start < end time ( because when curr start time [ 5 ] is less than heap end time [ 30 ] we need a different room so we push that end time)
        - different meeting rooms = size of array
        
        = why have min heap ?
        - if we had max heap we would keep inserting time ( considering different rooms ) even when meeting can be done 
        in same rooms
        - having "min end" time on top helps to see if next start time can have same meeting room or needs different meeting room
        - heap [ top 10 30 ] current start 15, this can be held in 10  wala meeting room , so we replace
        
        - "we replace" when curr start time > heap end time, considering that both meetings can be held in same room
    
        '''
        
        # SECOND ATTEMPT
        
        if len(intervals) == None or intervals == None:
            return 0
        
        intervals.sort()
        rooms = 1 # a room for 1st meeting
        minHeap = [] # [intervals[0][1]] # [30]
        heapq.heappush(minHeap,intervals[0][1])
        
        
        for i in range(1,len(intervals)):
            if minHeap[0] > intervals[i][0]: # if end time on top of minheap > current end time, new room needed
                rooms+=1
                heapq.heappush(minHeap,intervals[i][1]) # push the value
            else:
                heapq.heapreplace(minHeap,intervals[i][1]) # pop and push the value
                
                # OR pop and push
                # heapq.heappop(minHeap)
                # heapq.heappush(minHeap,intervals[i][1])
                
            #heapq.heapify(minHeap) # I do not need to heapify
            print(minHeap)
        
        print(rooms) # or just length of heap
        return rooms
        
        
        
        # FIRST ATTEMPT
        # intervals = []
        # intervals = [[none,none],[none,none]]
        
        #if len(intervals) == 0 or intervals == None:
        '''
        if not intervals: return 0
        
        #lamda = intervals.sort()
        intervals.sort()
        
        ans = [intervals[0][1]] # insert in the heap initially else the 
        
        for index in range(1,len(intervals)):
            
            # compare current start time with end time in heap
            # "curr time < top of heap"
            if intervals[index][0]<ans[0]: # intervals[index][0] is the current time, ans[0] is the top element ( end time )
                heapq.heappush(ans,intervals[index][1])
            else: 
                # "we replace" when "curr start time > heap end time" , considering that both meetings can be held in same room
                # pop the top and insert current == same as heapreplace
                heapq.heappop(ans)
                heapq.heappush(ans,intervals[index][1])
                
        return len(ans) # size of heap is k, thats the count of meeting rooms
        
        '''   
     

    
        
        # Mehod 1 : without heaps
        # Time complexity : O(n * nlog n) ,sorting time only
        # Space complexity : O(n) , prev_end_values
        
        '''
        - just store all end values in an array
        - if else condition below is important
        - we cannot have an prev_end_values as a vaalue, it has to be an array, so that we always get least end time first, try for this eg. [[9,10],[4,9],[4,17]]
        - if prev_end_values is an integeer, 3 roooms will be assigned, but actually only two should be assigned
        '''
       
        '''
            if len(intervals) == 0 or intervals == None:
            return 0
        # This is same as above
        # if not intervals: return 0
        
        intervals.sort()
        
        rooms = 1
        
        prev_end_values = [intervals[0][1]] # [30]
        
        for i in range(1,len(intervals)):
            if prev_end_values[0] > intervals[i][0]: # end time is higher than current start time, so new room needed
                rooms+=1
                prev_end_values.append(intervals[i][1])
            else : # same room can be used, so update the end time in prev_end_values
                prev_end_values[0] = intervals[i][1] # O(1)
                
            prev_end_values.sort() # sort n times == n*nlogn
            print(prev_end_values)
        
        print(rooms)
        return rooms
        
        '''
    
    
    
        # Method 3: chronological order
        # Time complexity :O(nlogn), sorting
        # Space complexity : O(n)
        
        '''
        - move start pointer and add rooms for every meeting
        - once meeting ends, reduce the room, as its free now and to make nullify unnecessary increase in the room
        - look into code for more explanation
        
        '''
        
        '''
        if len(intervals) == None or intervals == None:
            return 0
        
        intervals.sort()
        
        # sort start and end times
        start_times = sorted([ s[0]  for s in intervals])
        end_times = sorted([ s[1]  for s in intervals])
        
        print(start_times)
        print(end_times)
        start_time_pointer = 0
        end_time_pointer = 0
        L = len(intervals)
        rooms = 0
        
        # for i in range(L):
        while start_time_pointer<L: # until start pointer goes to the end of start_times
                
            print(start_time_pointer)
            print(end_time_pointer)
            
            if start_times[start_time_pointer] >= end_times[end_time_pointer]: # meeting ended, room is free
                rooms -= 1 # because one room is empty now, we subtract because everytime we are adding at the bottom, so its null
                end_time_pointer+=1
                
            # we always increase rooms for new start
            rooms += 1
            start_time_pointer+=1
                
            print("rooms",rooms)
        print(rooms)
        return rooms
        '''
        
                 
            
            
        