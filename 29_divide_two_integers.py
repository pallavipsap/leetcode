# Sept 7, 2020

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Time : O(log n)
        # shifting bits
        # Space : O(1)
        '''
        - understand bit shifting
        - shifting digits towards left once is multiplying by 2

        - Do not forget brackets here ldividend = ldividend - (ldivisor << numShifts)
        '''
        # edge case
        if dividend == 0:
            return 0

        # dividend = -2147483648
        # divisor = -1
        # 1<<31 = 2147483648
        if dividend == -(1 << 31) and divisor == -1:
            return (1 << 31) - 1

        # the code below also handles the cases where dividend > divisor
        # convert to positive numbers
        ldivisor = abs(divisor)
        ldividend = abs(dividend)
        numShifts = 0

        result = 0  # temporary dividend
        while ldividend >= ldivisor:  # 25 / 4 ; 9/4 ; 1/4 ( false )
            numShifts = 0
            ans = ldivisor << numShifts  # 4 << 0 = 4; 4 << 0 = 4

            while ans <= ldividend:  # 4<25, 8<25, 16<25, 32<25(false); 4<9 , 8<9, 16<9 ( false )
                numShifts += 1  # 1, 2, 3
                ans = ldivisor << numShifts  # 8, 16, 32

            numShifts -= 1  # go back by step 1 , 2 => shifts upto 16 ; 1 = shifts upto 8
            print(numShifts)
            result += 1 << numShifts  # 2^numShifts # 2^2 + 2^1

            print('result', result)

            ldividend = ldividend - (ldivisor << numShifts)  # 25 - 4^2 = 9; 9 - 8 = 1
            print('dividend', ldividend)
        print(result)

        # case : dividend > divisor, returns result which is 0
        if dividend < 0 and divisor < 0:
            return result
        if dividend > 0 and divisor > 0:
            return result
        return - result






