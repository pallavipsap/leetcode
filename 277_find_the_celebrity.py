# Look at your notes for explanation

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

'''
- everyone knows celebrity
- celebrity does not know anyone
- there is one or no celebrity

- knows(2,2) is true: a person knows himself [ **IMPORTANT]
- so we must not invoke knows(a,a), because then it will give us wrong result, celebrity will know himself but actually celebrity should not know anyone

Follow up question:
- in case multiple celebrities, use indegrees and out degrees to find all celebs ( probably a solution )
'''


class Solution:
    def findCelebrity(self, n: int) -> int:

        # Method 2 : Two iterations
        # Time : O(n)
        # Actually O(2n)
        # Space : O(1)

        celeb = 0
        for person in range(1, n):  # 1 to n-2

            # if assumed celebrity knows person, the persosn becomes a possible celebrity
            if knows(celeb, person):
                celeb = person

        # 1st iteration gives us only when
        for person in range(n):  # 0 to n-1

            # if celeb knows person - no celebrity
            # if person does not know celebrity - no celebrity found

            # we must check id celebrity and person are not same , because we know ourselves
            # hence if condition will become true when knows(celeb,person), and return -1 right away
            # basicaly we need not do anything if ( celeb is person ) knows(1,1)

            if person != celeb and (knows(celeb, person) or not knows(person, celeb)):
                return -1  # no celebrity found

        return celeb

        '''


        # Method 1 : O(n^2)
        # Time : O(n^2)
        # Space : O(1)

        # check all combinations to see if persons know each other
        # for a combination where we get; everyone knows a person, but the person does not know anybody; then that person is a celebrity
        # If we do not find any such combination, return -1 ( no celebrity )

        self.n = n

        # go from 0 to n-1
        # check if all celebs
        for i in range(n):

            # send al persons one by one 
            if self.isCelebrity(i): # celebrity found
                return i
        return -1

    def isCelebrity(self,celeb):


        for person in range(self.n):
            if celeb == person : continue
            if knows(celeb,person) or not knows(person, celeb):
                return False

        return True

        '''






