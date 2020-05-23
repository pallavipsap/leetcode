# Reference : https://www.youtube.com/watch?v=QdVrY3stDD4 ( two pass)
# Reference : https://www.youtube.com/watch?v=uN5QUBHUQaM ( Geeks for geeks - Improved solution one pass)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # one pass solution
        # here we know atleast one side of the mid will always sorted
        # look at the solution in the leet code and the one on scratch paper to understand

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            # 1st half is sorted, 2nd half is unsorted
            # print('1st half sorted')
            elif nums[mid] >= nums[
                start]:  # this part is sorted, mid is greater than start "1st half of array is sorted"
                if target >= nums[start] and target <= nums[mid]:  # target is in 1st half
                    end = mid - 1
                else:
                    start = mid + 1  # target is in 2nd half


            # 1st half is unsorted, 2nd half is sorted
            # nums[mid]<nums[start] i.e 1st half is unsorted then, 2nd half is obviously sorted so we check for target in 2nd half
            else:
                print('2nd half sorted')
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1  # target is in 2nd half
                else:
                    end = mid - 1  # target is in 1st half

            print('start', start)
            print('end', end)

        return -1
