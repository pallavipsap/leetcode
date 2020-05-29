# Updated on May 29 2020
# Done on May 16 2020

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # N is length of list
        # K is length of longest word in the list
        # in ordered dict we need not make sure that we have a  key already, we can create key while assigning the value
        # it does not give key error

        # Method 1 : Count the chars O(NK)
        # create a list of count as keys

        ans = collections.defaultdict(list)

        # I have to create the key count everytime I encounter the word so I put it inside for loop

        for str in strs:  # will run N times
            count = [0] * 26  # creates a list of 26 '0's
            print(count)  # this is just the list of 0s created for a string below

            for ch in str:
                count[ord(ch) - ord('a')] += 1  # increase the count for that particular character in count list

                # create a tuple of these unique counts and use them as keys in ans dict
                # I am converting count which was a list to tuple

                # lists are unhashable so we cannot have lists as keys

                ''' 
                # this works
                 if tuple(count) in dict:
                    dict[tuple(count)].append(str)
                else:
                    dict[tuple(count)] = [str]

                OR below
                '''
            # convert list to tuple
            ans[tuple(count)].append(str)  # when we encounter same count tuple, we append the i.e append the word

        return ans.values()

        '''
        #method 2  : Sorted strings O(NKlogk) 
        # create tuples of chars : use as keys
        # sorted is needed because for all words : ate tea eat the key is [a e t], this is a way to keep the key unique
        # but it adds log k time to the complexity to sort the keys
        #no ordered list

        dic={}
        for i in range(len(strs)): # i gives all strings  # runs **N times
            key1=tuple(sorted(strs[i])) # my key is  tuple of chars, sorting will take **KlogK times for longest string of length k

            # use sorted letters ( unique ) as keys
            if key1 in dic:
                dic[key1].append(strs[i])
            else:
                dic[key1]=[strs[i]]

        return dic.values()

        '''
























