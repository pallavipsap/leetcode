# Done on July 19
# works for duplicates too

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        '''
        edge cases :
        [0 1 6 8 9] = low crosses high towards right
        [0 1 2 5 6] = high crosses low towards left
        [0 1 2 5 6 7] = high crosses low towards left
        duplicates : [ 0 1 2 2 3 3 5 6 7]

        '''

        # Method 2 : Binary search
        # Time complexity : O(log n)
        # Space complexity : O(1)

        '''
        - since it is a sorted array, think of binary search
        - trick is to stop when low and high cross ( do not check criteria for equal, they must cross )
        - we go towards the place where there is "just" a gap between "citation values" and "diff"
        - take care of different values ( citation array values, diff, index ( low high mid) )
        - do not get confused with multiple values

        Problems :
        - check all edge cases to figure out return "n - low"
        - usually from previous questions, return has some modifications with low usually

        '''
        if citations == None or len(citations) == 0:
            return 0

        low = 0
        high = len(citations) - 1
        n = len(citations)

        while low <= high:  # while high and low have not crossed each other
            mid = low + (high - low) // 2
            diff = n - mid  # it is a series of descending numbers sarting from n
            if citations[mid] == diff:
                return diff
            elif citations[mid] < diff:
                low = mid + 1  # since mid is already checked we do mid+1
            else:
                high = mid - 1  # since mid is already checked we do mid-1
        print(n, low)
        return n - low  # low is the index and not diff value

        # Method 1 : Linear search O(n)
        # Time complexity : O(n)
        # Space complexity : O(1)

        '''
        - just go linearly and find the place where citation value is justtt " greater " than diff ( n - index) value
        '''

        '''
        if citations == None or len(citations) == 0:
            return 0

        n = len(citations) # start of numbering for h index
        for i in range(len(citations)):
            diff = n-i # len of citations - index of citation
            if citations[i] >= diff: return diff

        return 0

        '''




