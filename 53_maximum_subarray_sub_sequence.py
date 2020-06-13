class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # MAXIMUM SUBARRAY

        # eg. [-2,1,-3,4,-1,2,1,-5,4] ans is 12
        # eg. [ -3 -4 -1 -2 -5] ans is -1
       
        sum = nums[0]
        temp = [nums[0]]

        for i in range(1, len(nums)):

            if nums[i] >= sum + nums[i]:
                # sum[i] = nums[i]
                sum = nums[i]

            elif nums[i] < sum + nums[i]:
                sum = sum + nums[i]
            temp.append(sum)
            print(sum)  # gives all the sum

        print(temp)
        return (max(temp))


        # MAXIMUM SUBSEQUENCE
        # eg. [-2,1,-3,4,-1,2,1,-5,4] ans is 12
        # eg. [ -3 -4 -1 -2 -5] ans is -1
        # sum = [nums[0]]

        '''
        sum = nums[0]
        temp = [nums[0]]

        # Time complexity : O(n)
        # Space complexity : O(1)

        for i in range(0, len(nums) - 1):

            # running_sum = sum+nums[i+1]

            if (sum + nums[i + 1] > nums[i + 1]) and (
                    sum + nums[i + 1] > sum):  # if sum is greatest of all; eg. 5 4 3, 3 4 5,
                sum = sum + nums[i + 1]
            elif sum > nums[i + 1]:  # negative numbers : eg. -2 1
                sum = sum
            else:  # negative numbers : nums[i+1] > sum :  eg. 5 ,-3
                sum = nums[i + 1]

            print(sum)
            temp.append(sum)
            print(temp)



        '''
