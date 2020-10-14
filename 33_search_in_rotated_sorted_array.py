#May 22 2020
# a really good sum for binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
        - modified binary search
        - binary search only works when array is sorted
        - pivot is on unsorted side
        - find the point where array is rotated ( use binary search for this)
        '''
        # Time : O(log n), n is the length of array
        # Space : O(1)

        if len(nums) == 0 or nums == None:
            return -1

        # find the index where rotation occurs

        left = 0
        right = len(nums) - 1

        # ****go to unsorted side to find pivot
        # usually when you right left<=right, you have to mention a condition where if left == right: pivot = left break
        while left < right:  # do not make a mistake where left <= right
            mid = right + (right - left) // 2
            if nums[mid] > nums[
                right]:  # [ 4 5 6 7 0 1 2] ;mid = 7,right = 2, weird when array is sorted, right element is smaller, search on right
                left = mid + 1
            else:  # nums[mid] < nums[right] # [ 5 6 0 1 2 3 4] ; mid = 2, right = 4, thats good, but left is 5, so search on left
                right = mid  # right = mid and not mid-1 because it is still possible this mid element is the smallest in the array, i.e 2 can be the smallest element in the array

        # pivot found
        # pivot is on left or right , the point where right= left is the rotation point
        print(right)
        print(left)

        # now we are doing normal binary search with respect to the pivot
        # here we compare pivot to right, pivot to left
        '''
        Consider [4 5 6 7 0 1 2]
                          | 0 is pivot
        if target 4 and 7 (and not 0) : move to left[ 4 5 6 7 0]
        if target betweeen ( consider smallest element here ) 0 and 2 move to right [ 0 1 2]
        we do this basically because now the array is sorted on either sides

        '''
        # if nums[right]==target: return 0

        # now array divided into two sorted halves based on the start
        start = right  # or right i.e the pivot point i.e the smallest element
        left = 0
        right = len(nums) - 1

        '''
        #ask for case [ 5 6 0 1 2 3 4] target = 6
        # now we are arrangin the array so that we get sorted array eventually to do normal binary search
        if target>=nums[left] and target<=nums[start-1]: #[4 5 6 7]
            right = start-1 # search on left, make sure its start - 1 because start is the smallest point
        else: #[0 1 2]
            left = start # search on left, make sure we do not choose start+1, because then we lose value at index start

        '''
        # now check in which sorted half your target is present
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start

        print(left)
        print(right)

        # considers [ 5 6 0] in above case
        # now do normal binary search on the sorted part found above
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:  # target of left
                right = mid - 1
            else:  # target on right
                left = mid + 1

        return -1







