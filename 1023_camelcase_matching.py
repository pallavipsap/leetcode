# two pointer approach is very obvious as we are comparing the strings
# Time: O(mn)
# n words, length of largest word or pattern is m
# Worst case will be when we have to iterate through the largest word everytime, for every word
# Space : O(1), only comparisons no extra space
'''

edge cases:
- ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
- ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"] "FoBa" (FootBall, FoBaT)
- ["FooBarTest"], "FB"
- ["FooTestBar"], "FB"

- i is pointer for word
- j is pointer for pattern

'''


class Solution:

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        result = []
        for word in queries:

            # reset values
            flag = False
            w = len(word)
            j = 0  # bringing index in pattern to 0 again

            # iterating through every word
            for i in range(w):  # incrementing word index

                # since we are updating j everytime need to check if j is still less than pattern
                # once pattern length is reached this "if" will never be entered
                if j < len(pattern) and word[i] == pattern[j]:
                    j += 1  # incrementing pattern index
                    # if pattern ends at any point, eg. FooBar, FB
                    if j == len(pattern):
                        flag = True  # if there are no upper cases in word now , there are chances its True****

                # else when pattern length is reached or there is mismatch in word
                # eg. FooBar, FB

                # flag is false when FoorBarTest,FB; when remaining chars in word still have some uppercase****
                # flag is False when FooTestBar,FB; when B mismatched with T and T is capital

                # else condition skipped if FootestBar,FB; when B mismatched with t and t is capital
                # that means, if there is only mismatch, then else is skipped
                elif word[i].isupper():
                    flag = False
                    # once flag is false break, no point in going ahead
                    break

            result.append(flag)

        return result

        # My code which did not work
        '''
        p = len(pattern)
        result = []

        for word in queries:
            print(word)
            w = len(word)

            flag = False
            # comparing every word with pattern
            i,j = 0,0

            while i<w and j<p:

                if word[i]==pattern[j]:
                    i+=1
                    j+=1
                elif word[i].isupper() and pattern[j].isupper():
                    print('here')
                    result.append(False)
                    flag = True
                    break
                else:
                    i+=1
            if flag: break # result already modified

            if j<p:
                print('j<p')
                result.append(False)

            # pattern ends early    
            if j == p and not flag: # it means pattern ends here, and result still need to be found
                flag = True

                # Now we check if rest of the string has small cases

                while i<w:
                    print(word,'here')
                    print(word[i])
                    if word[i].isupper(): 
                        result.append(False)
                        flag = False
                        break
                    i+=1

                if flag: result.append(True)     

        print(result)
        return result




        '''


