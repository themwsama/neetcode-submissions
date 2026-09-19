class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, right = 0, len(matrix) * len(matrix[0]) - 1

        while left <= right:
            middle_value = (right - left) // 2 + left
            middle_row = (middle_value) // len(matrix[0])
            middle_col = (middle_value) % len(matrix[0]) 

            if target == matrix[middle_row][middle_col]:
                return True
            elif target < matrix[middle_row][middle_col]:
                right = middle_value - 1
            else:
                left = middle_value + 1

        return False

