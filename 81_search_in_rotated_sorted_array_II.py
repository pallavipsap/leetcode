# Reference : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/643895/Not-Pretty-Python
# May 23 2020

class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        # worst case time complexity = O(N)
        # best case : O(long N)

        if not nums: return False
        if len(nums) == 1: return nums[0] == target  # returns true if nums[0] is target else false

        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = (start + end) // 2
            if nums[mid] == target:
                return True

            # **********important case == only difference in ist and 2nd part
            # in cases where start end mid are equal: it will be difficult to know where the target is
            # look at elif and else conditions below, they are start<=mid else also means mid<=end, hence here both conditions will be true
            # so we put this condition here, where we ignore the ends if this case comes
            # [ 1 3 1 1 1], we remove ones ---> [ 3 1 1 1]
            if nums[start] == nums[mid] == nums[end]:
                start += 1
                end -= 1
            # Would this affect the run-time complexity? How and why?
            # For a case like this [ 1 1 1 1 1 1] target = 3 the complexity is O(N/2) == O(N)
            # because we shall keep on removing elements from both ends and not find the target element

            # left side is sorted
            elif nums[start] <= nums[mid]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            # right side is sorted
            else:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False