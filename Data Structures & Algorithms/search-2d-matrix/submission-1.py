class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0]) 
        def search(left, right, target):
            print(left, right)
            mid = (left+right)//2
            x = mid//w
            y = mid-(w*x)
            if matrix[x][y] == target:
                return True
            if right-left == 0:
                return False
            val = False
            if target < matrix[x][y]:
                val = search(left, mid, target)
            elif mid < right:
                val = search(mid+1, right, target)
            return val
        return search(0, h*w-1, target)
        