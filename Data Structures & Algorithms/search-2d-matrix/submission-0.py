class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row*col-1
        while left <= right:
            mid = (left + right) // 2
            r = mid // col
            c = mid % col
            val = matrix[r][c]
            if val == target:
                return True
            if val < target:
                left = mid + 1
            if val > target:
                right = mid - 1
        return False
