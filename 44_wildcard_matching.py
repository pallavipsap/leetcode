# Sept 4, 2020
# Good notes, good solution
# Check time complexity

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Method 2 : Two pointer
        # Time complexity : O(SlogP) ?
        # Best case : min(S,P), because one will go out of bound
        # Space complexity : O(1)
        '''
        - we use sp and pp to compare strings
        - sStar and pStar are just to help us backtrack
        - make sure pp does not go out of bound at every if condition
        - wcheck where to write 'if' or 'while' in the case below
        Cases:
        s = acdcb
        p = a*c?****** ( p is longer than s)
        '''

        # edge case
        if s == p or p == '*': return True
        if len(s) == 0 or len(p) == 0: return False  # either of the two string is blank

        s1 = len(s)
        p1 = len(p)
        sp = 0
        pp = 0
        pStar = -1  # initial value
        sStar = -1  # initial value

        while sp < s1:  # until sp goes out of bound
            # case 1: char match Found or '?'

            # make sure pp does not go out of bound at every if condition
            if pp < p1 and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1

            # Case 2 : Zero case
            elif pp < p1 and p[pp] == '*':  # increasing pp here so check for out of bound
                # Case 2 : Zero case
                pStar = pp
                sStar = sp
                pp += 1  # here we only increase pp as pp is '*' and we do not match it to anything, so no need to increment pp

            # Case 3 : We never found a '*', and mismatch found, nothing to cover up so straight False
            elif pStar == -1:  # since Case 1 and 2 fails, it means this is a char mismatch
                return False

            # Case 4 : char mismatch inspite of '*'
            else:  # implicitly it means p[pp]! = s[sp]
                pp = pStar + 1  # restore pp position

                # Once case: skip character in main 's' string
                sStar += 1  # increase sStar
                sp = sStar  # here is where sp skipped one char, so we cleverly matched '*' in p, to this one char in 's'

        # Special Case:
        # p is longer than s
        # s = acdcb
        # p = a*c?****** ( p is longer than s)

        while pp < p1:
            print('in')
            if p[pp] != '*':
                return False
            pp += 1  # until we get only '*' at the end of p, keep increasing pp

        return True

        # Method 1 : DP
        # Time complexity : O(n^2); form matrix
        # Space complexity : O(m * n)
        # O(m+1 * n+1) space ideally
        '''
        - 0 case comes from row above
        - 1 case comes from diagonal up
        - No for loop for "*"" case

        '''
        '''
        #edge case
        if s == p or p =='*': return True
        if len(s) == 0 or len(p)==0: return False

        # form matrix
        p1 = len(p) # rows = p1 + 1
        s1 = len(s) # cols = s1 + 1
        # p1+1 rows, s1+1 cols, rows inside cols outside, dummy value = 0
        dp = [[ 0 for col in range(s1+1)] for row in range(p1+1)]
        #print(dp)

        dp[0][0] = True

        for i in range(1,len(dp)): # i = 1 to len(dp)-1, we start from 1 because dp[0][0] is already filled

            if p[i-1] == '*': # i-1 because i starts from 1

                # Zero case for first col; No one case here
                dp[i][0] = dp[i-1][0]  # filling first col from above value ( row above) in that column

                j = 1
                # for all colums except first col
                while j<len(dp[0]): # all columns in that row
                    # zero and  one case
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-1] # row above OR diagonal up

                    # if once true the whole row is true ( - abcde matches -a*)
                    if dp[i][j] == True:
                        while j < len(dp[0]): # make all cols true
                            dp[i][j] = True
                            j+=1
                    # do not increment this j, before checking true condition ; if dp[i][j] == True:
                    j+=1 # increase j here, because if the "if" condition is false then we need to increment j


            elif p[i-1] =='?':
                for j in range(1,len(dp[0])): # cols
                    dp[i][j] = dp[i-1][j-1]

            else: # normal char
                for j in range(1,len(dp[0])): # cols
                    dp[i][j] = p[i-1]==s[j-1] and dp[i-1][j-1] # char matches AND diagonal up is True else False

        return dp[p1][s1]

        '''







