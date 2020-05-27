# May 27 2020

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        '''
        m rows, n cols
        Two ways possible :

        1. Search in every mth row with binary search  == m * log n
        2. Search right mth row to perform binary search == m + logn
        So done with 2nd method

        '''

        if matrix == [[]] or matrix == []:
            print('here')
            return False

        row = len(matrix)  # number of rows
        col = len(matrix[0])  # number of cols
        flag = 0
        # print(row,col)

        for r in range(row):
            print('in')
            if target <= matrix[r][col - 1]:  # last element of every row
                flag = 1
                print(matrix[r][col - 1], matrix[r])

                # if target == matrix[r][col-1]:
                # return True
                break
        '''

        '''
        if flag:

            # using matrix to find the right element in a given row

            l = 0
            h = len(matrix[0]) - 1

            # l = matrix[r][0] #1st element in that row
            # h = matrix[r][col-1] #last element in that row

            print(l, h, 'here')
            while l <= h:
                mid = l + (h - l) // 2
                print(matrix[r][mid])

                if matrix[r][mid] == target:
                    return True

                elif target > matrix[r][mid]:
                    l = mid + 1
                    # col+=1

                else:  # target is on left, move to left
                    h = mid - 1
                    # row-=1

            # using a separate list res = matrix[r] instead of matrix
            # it should add one more datastructure list which is nt necessary

            '''
            print(res)
            l = 0
            h = len(res)-1
            print(l,h,'here')
            while l<=h:
                mid = l+(h-l)//2
                print(res[mid])

                if res[mid] == target:
                    return True

                elif target>res[mid]:
                    l = mid+1

                else: # target is on left, move to left
                    h = mid-1
            '''


        else:
            return False