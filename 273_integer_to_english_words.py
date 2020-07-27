# Done on July 26, 2020
# referred sum from video
# need to think of solution, implementation is easy
# self.num not used

class Solution:
    def numberToWords(self, num: int) -> str:

        # Time complexity - O(n)
        # traversed only once
        # Space complexity - O(1)
        # the arrays below are also of constant space

        self.below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                         "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        thousands = ["", "Thousand ", "Million ", "Billion "]  # need spaces here

        '''

        self.num = num
        if self.num == 0: return "Zero"
        result = ""
        i = 0
        while self.num > 0 :
            if self.num%1000 != 0:
                result = self.helper(num % 1000) + thousands[i] + result # vey important 
            i+=1
            self.num = self.num//1000
        result.strip()

    def helper(self, num):
        if self.num == 0 : 
            return ""
        elif self.num<20:
            return self.below_20[self.num] + " "
        elif self.num<100:
            return self.tens[self.num//10] + " " + self.helper(self.num%10)
        else:
            return self.below_20[self.num//100] + " Hundred " + self.helper(self.num%100)


        '''

        if num == 0: return "Zero"
        result = " "
        i = 0
        while num > 0:
            if num % 1000 != 0:
                result = self.helper(num % 1000) + thousands[i] + result  # vey important
            i += 1
            num = num // 1000
        return result.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.below_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.below_20[num // 100] + " Hundred " + self.helper(num % 100)

