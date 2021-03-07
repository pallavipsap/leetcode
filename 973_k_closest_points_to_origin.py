#Refer : https://www.youtube.com/watch?v=eaYX0Ee0Kcg good one
#May 27 2020

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        # Remember other version can be list of tuples
        # Similar to K smallest elements in a given array
        
        
        # Method 2: Creating a heap O(k+(N-k)logk)
        # Time:  O(n) to calculate dist +  O(nlogk)
        # Space : O(k)
        
        # If I go for minheap , everytime my **top min element** will be replaced by current min element
        # heap  = [ 50 60 70 ] if curr = 20 , if 20 < top(50) (replace 50 by 20 ) new min heap = [ 20 60 70]
        
        # Even if I compare current element with last element in max heap inside if : 
        # if heap[-1] i.e. 70 > curr i,e 20 , heappush will alwats replace the top element so 50 will be replaced in this case
        # op will still be [ 20 60 70 ]
        
        # So I go for ***max heap : so current max element will be replaced by current smaller element
        # i.e heap  = [ 80 60 50 ] if curr = 20 , if 20 < top(80) (replace 80 by 20 ) new max heap = [ 60 50 20]
        # So my max heap will start gathering all smallest elements
        
        dist = []
        for p in range(len(points)): #( RUNS N-k times)
            
            
            # list of tuples of three, 1st element is negative for max heap
            dist.append(( -(points[p][0]**2 + points[p][1]**2) , points[p][0], points[p][1] ))
            #dist.append(points[p][0]+abs(points[p][1]))
            
        #print(dist)
        
        #print(dist)
        heap = [] # heap of tuples
        
        # Aim is to replace highest absolute value from minheap
        # so replacing lowest negative value ( highest absolute value ) i.e. in [-80 -70 -60] will allow insertion of new lowest absolute value 20
        
        # MAX HEAP : push entire tuple in heap, but sort by euclidean dist
        
        
        for p in dist: # p is a tuple ( RUNS **N-k times )

            if len(heap)<K: # Heap creation runs **O(logk)
                heapq.heappush(heap,p) # insert only dist i,e. p[0]
            elif p[0] > heap[0][0]: # point value in top element hence [0][0] == heap top < new elem
                print(heap[-1])
                heapq.heapreplace(heap,p)

        #print(heap)
        res = []     
        for p in heap:      # ( RUNS k times **O(k) )
            res.append([p[1],p[2]])
           
            
        print(res)
        return res
            
        
        
        # Method 1 : With lambda
        # Sort according to euclidean distance Nlog N === sorting basically takes nlogn
        '''
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
        '''
        
        
        
        # Method 1 : Longer approach without lambda
        # Time : O(n) for calculating dist + O(nlogn) to sort
        # Space : O(n), create new list with sorted distances
        
        # Sort according to euclidean distance Nlog N === sorting basically takes nlogn
        # create tuples of [(dist,p1,p2), (dist,p1,p2)....] this will sort list according to dist
        
        '''
        
        dist = []
        for p in range(len(points)):
               
            # list of tuples of three
            dist.append((points[p][0]**2 + points[p][1]**2,points[p][0],points[p][1]))
            #dist.append(points[p][0]+abs(points[p][1]))
            
        #print(dist)
        
        dist.sort()
        #print(dist)
        
        res = []
        finalres = []
        for i in range(K):
            
            res.append(dist[i][1])
            res.append(dist[i][2])
            print('r',res)
            finalres.append(res)
            res = []
        
        #print('f',finalres)
        return finalres
        
        '''
        
        
    
    
     
        
        