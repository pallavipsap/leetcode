class Solution:
    #May 22
    def searchInsert(self, nums: List[int], target: int) -> int:

        # binary search : make sure to return only low always:Time O(logN), Space O(1)
        # typical binary search logic applied, we return low or high in binary search , here we return only low
        # try with cases
        # [1,3,5,6],0 : low = 0, h = -1, return low
        # [1,3,5,6],8 : low = 4, h = 3, return low
        # [1,3], 0: low = 0, h = -1, return low
        # [1,3,5],8 : low = 3, h = 2, return low

        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                print(target)
                print('ans', mid)
                return mid
                # break
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        print(l)
        return l


