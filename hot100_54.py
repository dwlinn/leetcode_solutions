from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        result = []
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            # 从左向右
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            # 从上到下
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            # 从右到左
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
            bottom -= 1
            # 从下到上
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
            left += 1
        print(result)
        return result


Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
