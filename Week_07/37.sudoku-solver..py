from typing import List
import collections


class Solution:
    """
    37.解数独 https://leetcode-cn.com/problems/sudoku-solver/
    """

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(board, row, col, ch):
            for i in range(9):
                if board[row][i] == ch:
                    return False
                if board[i][col] == ch:
                    return False
                if board[(row//3)*3 + i//3][(col//3)*3 + i % 3] == ch:
                    return False
            return True

        def backtrack(board, row, col):
            m = n = 9
            if col == n:
                return backtrack(board, row+1, 0)
            if row == m:
                return True
            for i in range(row, m):
                for j in range(col, n):
                    if board[row][col] != '.':
                        return backtrack(board, i, j+1)
                    for ch in range(1, 10):
                        if not isValid(board, i, j, str(ch)):
                            continue
                        board[i][j] = str(ch)
                        if backtrack(board, i, j+1):
                            return True
                        board[i][j] = '.'
                    return False
            return False

        backtrack(board, 0, 0)


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(sol.isValidSudoku(board))
