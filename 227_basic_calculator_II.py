class Solution:
    def calculate(self, s: str) -> int:

        # edge case
        '''
        - "14-3/2"
        '''
        stack = []
        numsum = 0
        result = 0
        n = len(s)
        if not s: return 0

        lastSign = '+'  # ask interviewer
        for i in range(len(s)):  # its a character , not number

            c = s[i]
            if c.isdigit():  # take complete number hence multiply by 10
                numsum = numsum * 10 + int(c)  # c is a char so we do int(c)
                # c = c*10 + c - ord('0') # By calculating ascii character
                # eventually c is a number
            # print(sum)

            if ((not c.isdigit()) and (c != ' ')) or i == n - 1:  # it is a sign
                if lastSign == '+':
                    stack.append(numsum)
                elif lastSign == '-':
                    stack.append(-numsum)
                elif lastSign == '*':
                    stack.append(stack.pop() * numsum)
                elif lastSign == '/':
                    stack.append(int(stack.pop() / numsum))  # -3//2 = -2 ( problem ) #-3/2 = 1.5 ( correct)
                # print('in',stack)
                numsum = 0  # now we are getting ready for next number so 0
                lastSign = c  # that is current character / current sign
        # print(stack)

        while stack:
            result += stack.pop()

        print(result)
        return result







