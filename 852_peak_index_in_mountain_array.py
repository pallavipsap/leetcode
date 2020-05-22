class Solution:

    #May 22, 2020
    # recursive approach
    '''
     def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 0
        h = len(A)-1
        print(l)
        print(h)
        x = []
        res = self.recursive_bin(A,l,h)
        return res

    def recursive_bin(A,l,h):
        print(A)
        if l == h:
            print(l)
            return l
        else:
            mid = (l+h)//2
            if A[mid+1]>A[mid]:
                self.recursive_bin(mid+1,h)
            else: #if A[mid-1]>A[mid]
                self.recursive_bin(l,mid-1)
    '''

    # Binary search : log(N), iterative approach

    l = 0
    h = len(A)-1

    while l<=h:
        mid = (l+h)//2
        print('mid',mid)
        if A[mid+1]>A[mid]:
            l=mid+1
            print('l',l)
        elif A[mid-1]>A[mid]:
            h=mid-1
            print('h',h)
        else:
            return mid

    



    

