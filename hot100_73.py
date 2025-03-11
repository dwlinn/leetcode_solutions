from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
        """
        rows = set()  # 记录需要置0的行
        cols = set()  # 记录需要置0的列
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                value = matrix[i][j]
                if value == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        使用标记变量记录第一行和第一列是否存在0, 再用第一行第一列存储其他行列是否存在0
        """
        m, n = len(matrix), len(matrix[0])
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0

        if flag_row0:
            for i in range(n):
                matrix[0][i] = 0


Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
