# Refer 33. Search in Rotated Sorted Array
# Done on May 23 2020

class Solution:
    def findMin(self, nums: List[int]) -> int:

        # no duplcate elements
        # we have to move towards unsorted part
        # it is quite possible both parts are
        start = 0
        end = len(nums) - 1
        '''
        while start<=end:

            mid = (start + end)//2
            if start==end: #same thing is done by the above code, the moment start=end, we return
                print (nums[mid])
                return nums[mid]


            if nums[mid]>nums[end]: #right side of array unsorted [ 4 5 6 7 0 1 2] mid = 7, end = 2
                start = mid+1
            else: #left side unsorted, nums[start]>nums[mid] [ 7 8 1 2 3 ] start = 7, mid = 1
                end = mid
            print(nums[start:end+1])    
            print(nums[mid])


        '''

        # remember when start< end ( NOT start<=end)
        # possibly end = mid ( NOT mid - 1)
        # there should be something to make up for that '='
        # eg. [ 4 5 0 1 2]

        while start < end:

            mid = (start + end) // 2
            if nums[mid] > nums[end]:  # right side of array unsorted [ 4 5 6 7 0 1 2] mid = 7, end = 2
                start = mid + 1
            else:  # left side unsorted, nums[start]>nums[mid] [ 7 8 1 2 3 ] start = 7, mid = 1
                end = mid
            print(nums[start:end + 1])
            print(nums[mid])

        # basically the loop will break when start == end
        # same thing is done by the above code, the moment start=end, we return
        return nums[start]

