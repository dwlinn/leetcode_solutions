from typing import List


class Solution:
    """编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
    每行的元素从左到右升序排列。
    每列的元素从上到下升序排列。
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # 从矩阵右上角元素开始遍历，它是该行的最大值，同时是该列的最小值。
        i, j = 0, n - 1
        while i < m and j > -1:
            print(matrix[i][j], target)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


print(
    Solution().searchMatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
            [19, 22, 26, 28, 32],
        ],
        3,
    )
)
