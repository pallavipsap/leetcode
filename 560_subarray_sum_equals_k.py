# Look at all the solutions in leetcode: https://leetcode.com/problems/subarray-sum-equals-k/solution/
# look at notes made for this
# Two sum approach
# Done on May 29 2020


# brute force: O(N^3)
# subarray 0(N^2), calculating sum O(N)
# using two pointers static and moving poniters: and then storing sum with all the combinations

# method 2:0(N^2), Space O(N)
# calculate sum array (O(N))
# using the sum array using two pointers to find sum = k

# method 3:0(N^2), Space O(1) ==== sensible
# Find sum while iterating over the pointers

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # hashmap of cumulative sum :
        # distance between two points
        # key is sum, value : count of how many times we have seen that sum
        # if sum - k in hashmap, then we update the count

        dict = defaultdict(lambda: 0)
        dict = {0: 1}  # for sum=0, we have count = 1, this is when we encounter  7 - 7 = 0

        # cumulative sum of nums encountered
        cumsum = 0

        # count of number of subarrays of size k
        count = 0

        for n in nums:

            cumsum += n
            if cumsum - k in dict:  # whenever we find sum-k in dict, we found sum=k between two points
                count += dict[cumsum - k]

            # store cumsum in the dict
            # update the count of sum in cumsum already present
            dict[cumsum] = dict.get(cumsum, 0) + 1  # if num is not present

            # print(dict)
            print(count)

        return count


