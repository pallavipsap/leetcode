# Bit manipulation
# follow up question 260. Single Number III

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Method 3: Bit Manipulation
        # Time complexity: O(n)
        # Space complexity: O(1)
        '''
        - use the logic XOR with itself gives us "0" ( Remember)
        - XOR wih "0", gives the number itself ( Rememeber)
        - XOR with different no. gives us a different number
        - we start with bitmask 0, because XOR with 0 a number wil give number itself

        '''
        bitmask = 0
        for n in nums:
            bitmask ^= n
            print(bitmask)
        print(bitmask)
        return bitmask

        # Method 2: Hashset
        # Time complexity: O(n)
        # Space complexity: O(n)

        '''
        - keep putting number in hash set, and remove if we get the same number and return that number
        '''

        # Method 1: Hashmap
        # Time complexity: O(n)
        # Space complexity: O(n)

        '''
        hash_tab = {}
        for i in nums :
            try:
                hash_tab.pop(i) # will try to keep popping the element, if it exists in the table
            except:
                hash_tab[i] = 1 # if element does not exist then insert and give count 1
        return hash_tab.popitem()[0] # return the first item in hash_tab
        '''



