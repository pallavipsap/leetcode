# Sept 7, 2020

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        # Method 2: Bit manipulation
        # Time: O(n)
        # Space : O(1)
        # constant space ( binary number will only take the space)

        '''
        - XOR of number itself cancels each other hence we do two bitmask
        - 2's complement gives the rightmost significant bit

        eg. [ 1 2 1 4 9 2]

        - bitmask1: gives a combination of two single numbers in it (  z= x+y, here we obtain z)

        - bitmask 2: Use this to retrieve x or y.
        - if the diff==0 :
        we push 2 4 2 ==> retrieve 4

        - if the diff==1 :
        we push 1 1 9 ==> retrieve 9

        - XOR and get another number


        '''

        bitmask = 0
        for n in nums:
            bitmask ^= n
        print(bitmask)  # eg. combination of 4 and 9 ( two single numbers)

        # bitmask AND its 2's complement
        diff = bitmask & (-bitmask)

        # number goes into the bitmask its AND operation with diff != 0

        bitmask2 = 0
        for n in nums:
            if diff & n == 0:
                bitmask2 ^= n

        # second bitmask gives a single number
        # XORing combination of 4 and 9, and single number gives the other number
        return [bitmask2, bitmask2 ^ bitmask]

        # Method 1: Hashmap
        # Time: O(n)
        # Space : O(n)

        '''
        hashmap = Counter(nums)
        return [x for x in hashmap if hashmap[x] == 1]
        '''


