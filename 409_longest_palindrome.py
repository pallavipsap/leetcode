# May 30 2020

class Solution:
    def longestPalindrome(self, s: str) -> int:

        # Time complexity : O(N), space: O(1)
        # here we just have to create longest palindrome from the given letters in a string
        # we do not haev to find a palindrom created by the substrings
        # we haev to create our own palindrome, by the given letters

        length = 0
        # count all the chars
        count = collections.Counter(s)
        print(count)
        odd_added = 0
        longest = 0
        flag = 0

        for c in count:
            print('c', c)
            # for both odd or even count
            # even count : count[c]//2*2 takes all the values
            # odd count : We can still take max even count from it
            if count[c]:
                print(count[c])
                longest += count[c] // 2 * 2  # 5//2 * 2 = 4, this will take maximum even values

                # at any point in result, if result is even, we can put an odd char,if we have any odd count
                # this will be true only onceif odd letter has been addded, because length of resultant string will be odd here on,
                # so longest % 2 will be 1 afterwards
                if longest % 2 == 0 and count[c] % 2 == 1:  # aabb == aacbb
                    longest += 1

            print(longest)
        return longest

        # this also works
        '''

        counts = Counter(s)
        odd_added = False
        longest = 0
        for c in counts:
            if counts[c] % 2 == 0:
                longest += counts[c]
            elif odd_added is False:
                longest += counts[c]
                odd_added = True
            else:
                longest += counts[c] - 1
        return longest



        '''