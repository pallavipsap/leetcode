# referred solution
# many downwards
# May 23 2020


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # linear search is possible by just stopping when letter greater than target is found

        # binary search

        l = 0
        r = len(letters) - 1

        while l < r:

            mid = l + (r - l) // 2
            print(letters[l:r + 1])
            print(l)

            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid

            print(letters[l:r + 1])
            print(l)

        # better try this
        # [ c f j] target g
        if letters[l] > target:  # if stil last letter is greater than target,
            print(letters[l])
            return letters[l]

        return letters[0]  # [ c f j] target z

        '''
        print(letters[l % len(letters)])
        return letters[(l+1) % (len(letters))]

        # works when l = len(letters)
        # explanation a bit weird

        '''





