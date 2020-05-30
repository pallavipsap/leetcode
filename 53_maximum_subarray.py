class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # time complexity O(N)
        print(nums)
        l = len(nums)
        sum = nums[0]
        temp = [nums[0]]  # array of sums at every point
        for i in range(len(nums) - 1):
            if sum + nums[i + 1] >= nums[i + 1]:  # if current sum + new number is > than new number
                sum = sum + nums[i + 1]  # update the sum by adding the new number

            elif sum + nums[i + 1] <= nums[i + 1]:  # if current sum + new number is < than new number
                sum = nums[i + 1]  # update sum to new number itself
            temp.append(sum)
        print(temp)
        return max(temp)


