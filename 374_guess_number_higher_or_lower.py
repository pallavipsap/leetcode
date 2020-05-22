# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
#May 22 2020
class Solution:
    def guessNumber(self, n: int) -> int:
        # many downwards

        # binary search: Time O(logN) Space: O(1)
        # Consider A as an array of numbers 1 to N
        # instead of writing A[mid]< or > target, we are using numbers -1, 0 , 1

        # choose from 1 to n
        # consider indexes in arrays are numbered from 1 to n

        l = 1
        h = n

        # send the index ( mid ) to the guess API
        # here we definitely know correct number is present so we return when g==0
        while l <= h:
            mid = (l + h) // 2
            g = guess(mid)  # returns -1, 1, 0
            print(g)
            if g == 0:  # congrats correct number guessed
                return mid
            elif g == 1:  # number is higher than the mid, move right , target > A[mid]
                l = mid + 1
            else:
                h = mid - 1
