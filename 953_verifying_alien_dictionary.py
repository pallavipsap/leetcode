# from collections import OrderedDict
# follow up question:
'''
- if we have to give correct order then implement a custom sort ( follow up ques if asked)
'''
'''
- remember we are implementing a non sorted function, so if words are not sorted function returns True and our main function returns False
'''
class Solution:
    global letter_map
    letter_map = {}

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # Time: O(m * n)
        # n words, m is avg length of words
        # Space : O(1)

        count = 0
        for i in range(len(order)):
            # count+=1
            letter_map[order[i]] = i + 1

        print(letter_map)

        for i in range(len(words) - 1):

            # send two words to nonSorted function
            if self.notSorted(words[i], words[i + 1]):  # if function gives True then words are not sorted
                print('here')
                return False

        return True

    # NOT SORTED
    def notSorted(self, word1, word2):

        first = len(word1)
        second = len(word2)

        i = 0

        # one way of doing this
        '''

        while i<first and i<second:
            fc = word1[i]
            sc = word2[i]
            if letter_map[fc]>letter_map[sc]:
                return True
            elif letter_map[fc]<letter_map[sc]: # hello, leetcode; order = 
                return False
            i+=1

        # [apple, app] ==> false
        if first>second: return True

        '''
        # more efficient
        # second way of doing this

        while i < first and i < second:
            fc = word1[i]
            sc = word2[i]
            if fc != sc:
                # hello , leetcode; order = "hlabcdefgijkmnopqrstuvwxyz" -> returns False
                # words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz" -> returns True
                return letter_map[fc] > letter_map[sc]
            i += 1

        # [apple, app] ==> false
        return first > second

        return False






