# March 3, 2021

class UndergroundSystem:
    
    # Time Complexity : O(1), just calling dictionaries
    # Space complexity: O(P + S^2)
    
    # len of users :O(P)
    # Nested Dictionaries:
    
    '''
    Consider three stations A, B, C
    
    Avg times  ={
          A : ( B : {total time, total passengers},  C : {total time, total passengers})
          B : {  A : {total time, total passengers} ,  C : {total time, total passengers}}
          C : {  A : {total time, total passengers},  B : {total time, total passengers}}
    }
    
    This gives S^2 complexity, every station has all other staions in its values
    There can be any number of passengers travelling in these three stations
    
    This question is easym, because the question says you will always have a passenger checking out, and then checking in.ELse it would be complicated
    
    '''

    def __init__(self):
        self.users = {}
        
        # {45 : ["leyton",3]}
        
        self.avgTimes = {}
        # avgTimes = {
        #     startStation : { endStation , time diff , count }
        #     "leyton" : {"waterloo", time diff , count} 
        # }

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id] = [stationName,t] # add list  = [start station , start time] to the specific user

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        enterStation, enterTime = self.users[id] #  {45 : ["leyton",3]} enterstation = leyton , entertime = 3
        diff = t - enterTime
        
        if enterStation not in self.avgTimes:
            self.avgTimes[enterStation] = {}
        if stationName not in self.avgTimes[enterStation]: # check for checkout station name in they value
            self.avgTimes[enterStation][stationName] = [0,0] # dummy total time and count
            
        p1,p2 = self.avgTimes[enterStation][stationName]
        self.avgTimes[enterStation][stationName] = [p1+diff,p2 + 1]
        #p1 = p1 + diff # add time diff to original total time
        #p2 += 1 # add count of total users
        
        del self.users[id] # delete the user

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        p1,p2 = self.avgTimes[startStation][endStation]
        return p1/p2
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)