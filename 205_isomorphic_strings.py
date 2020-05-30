# May 29 2020

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        '''
        dict = {}

            for i in range(len(s)):
                    #print(dict.items())

                    if t[i] in dict.values():
                        if s[i]!=list(dict.keys())[list(dict.values()).index(t[i])]:
                            return False



                    # making sure value is same for repeated value in s
                    if s[i] in dict:
                        print(dict[s[i]])
                        print('1st',s[i],t[i])
                        if dict[s[i]]!=t[i]:
                            print('OUT')
                            return False

                    else:
                        dict[s[i]]=t[i]

            print(dict)
            return True

        '''

        dict = {}

        # chars in s as keys, chars in t as values

        for i in range(len(s)):

            # if key is present in dict
            # check if dict's value matches with current value "s"
            if s[i] in dict:
                if dict[s[i]] != t[i]:  # values does not match the current
                    print(dict)
                    return False  # eg. t = "eggg" s = "addw" , last letter g (key) is already present but value does not match with w


            # before entering new key, check if value exists
            else:
                if t[i] in dict.values():  # if new key is not present in dict, but new value is already present, means value is linked to another key
                    return False  # eg. t = "lat" s = "foo" gives false

                else:  # key is not present, value is not present, link both as usual
                    dict[s[i]] = t[i]

        return True
