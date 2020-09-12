# Sept 11, 2020

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # solution 3 : One pass
        # Time : O(n)
        # SPace : O(1)

        '''
        - keep track of min value; compare with current value and update min
        - keep track of max profit; curr val - min val ; update if max profit < curr profit
        '''

        if len(prices) == 0 or prices == None:
            return 0

        min_price = float("inf")  # positive infinity
        max_profit = float("-inf")  # or 0

        for i in range(len(prices)):

            if prices[i] < min_price:
                min_price = prices[i]
            print('min_price', min_price)

            cur_profit = prices[i] - min_price
            if cur_profit > max_profit:
                max_profit = cur_profit
            print('max_profit', max_profit)

        print(max_profit)
        return (max_profit)

        # solution 2 : One Pass - Buy and sell Dp problem
        # Time : O(n)
        # SPace : O(1)
        '''
	    dp = []
        subarray = []

        #print(prices.sort(reverse=True))
        #check descending

        if len(prices) == 0:
            return 0


        #print (prices)
        cur = prices[0]
        counter = 0

        for i in range(len(prices)) : # 0 1 2 3 4 5
            #print(i,'i')
            cur_id = i
            #print(cur_id,'id')
            for sub in range(cur_id,len(prices)):
                #print(sub)
                if prices[cur_id]<prices[sub]:
                    #print('to be checked with',prices[sub])
                    subarray.append(prices[sub])
            #print(subarray)
            dp.append(subarray)
            subarray = []
        #print('dp',dp)


        final_array = []
        for i in range(len(dp)):
            if dp[i]==[]:
                dp[i] = 0
            else :
                dp[i] = max(dp[i]) - prices[i]
        #print(dp)
        print(max(dp))
        return max(dp)

        '''
        # solution 1
        # Two pass : time limit exceeded solution
        # Time: O(n^2)
        # Space : O(1)

        '''
        maxprofit = float("-inf")
        for i in range(len(prices)):
            print(i)
            #inner = i+1
            for j in range(i+1,len(prices)):

                curr_profit = prices[j] - prices[i] # sell - buy
                #print(i,curr_profit,'curr')
                if curr_profit > maxprofit:
                    maxprofit = curr_profit
            #print(maxprofit)

        #print(maxprofit)
        if maxprofit < 0 :
            return 0
        else : return maxprofit

        '''






















