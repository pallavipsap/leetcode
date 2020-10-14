# Reference : https://www.youtube.com/watch?v=QdVrY3stDD4 ( two pass)
# Reference : https://www.youtube.com/watch?v=uN5QUBHUQaM ( Geeks for geeks - Improved solution one pass)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''

        - remember to use mid + 1, mid - 1, else r and l will never cross each other
        - ***when we divide the array, one half is sorted, other half is unsorted
        - go to the sorted side of the array , check if target exists, if not go to unsorted side
        - remember that any half can be unsorted hence we need to else ifs

        '''

        # Method 2  :  One - pass
        # Time : O(logn)
        # Space : O(1)

        if len(nums) == 0 or nums == None:
            return - 1

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2
            print(nums[l], nums[r], nums[mid])

            if nums[mid] == target:
                print(mid)
                return mid


            # if left is sorted, check target on left
            elif nums[l] <= nums[mid]:  # left is sorted
                if target <= nums[mid] and target >= nums[l]:
                    r = mid - 1  # move to left target is on left
                else:
                    l = mid + 1  # move to right, target is on right

            # if right is sorted, check target on right
            elif nums[r] > nums[mid]:  # right is sorted
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1  # move to right, target is on right
                else:
                    r = mid - 1  # move to left target is on left

            # combine both conditions : this works too
            '''
            elif ((nums[l] <= nums[mid]) and ( target<=nums[mid] and target>=nums[l] ) ) or ((nums[r]>nums[mid]) and not (target>=nums[mid] and target<=nums[r] )): # add not condition
                r = mid - 1 # target on left
            else: 
                l = mid + 1 # target on right

            '''

            # Here I am going to unsorted side, do not make this mistake
            '''
            [4,5,6,7,0,1,2] target 0
            - going to sorted side is easier, because we just check target 0 betweej 4 and 7 else go to right
            - if we go to unsorted side , we check if 0 is between 7 and 2, which it is, but it gives incorrect ans


            elif nums[r]<=nums[mid]: # right is unsorted
                if target <= nums[r]:
                    l = mid # go to right
                else:
                    r = mid # go to left

            elif nums[l]>nums[mid]: # left is unsorted
                if target >= nums[l]:
                    r = mid # go to left
                else:
                    l = mid

            '''

        return -1
