# Reference : https://www.youtube.com/watch?v=dnlB0lvz5LY
# similar to 205. isomporphic strings
# May 29 2020

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:

        # Time complexity : O(N)
        # N is the length of pattern or list of str : considering we go ahead only if both are same
        dict = {}
        # print(type(str)) # a string
        # split the strings by space, this will convert str into list of str
        str = str.split()
        print(str)  # this is a list

        # print(type(str)) # a list

        # length of list not equal to length of pattern
        if len(pattern) != len(str):
            return False

        # letters in pattern as keys, words in list(str) as values

        for i in range(len(pattern)):

            # if key is present in dict
            # check if dict's value matches with current value "s"
            print(pattern[i])
            if pattern[i] in dict:
                if dict[pattern[i]] != str[i]:  # values do not match the current

                    return False  # pattern : abba , str = dog cat cat cat

            else:
                if str[
                    i] in dict.values():  # if new key is not present in dict, but new value is already present, means value is linked to another key
                    return False  # eg.pattern = abbc, str = dog cat cat cat

                else:  # key is not present, value is not present, link both as usual
                    dict[pattern[i]] = str[i]
                    print(dict)

        print(dict)
        return True
