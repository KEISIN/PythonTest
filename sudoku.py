import numpy as np
def is_valid(board, row, col, num):
    if num in board[row, :] or num in board[:, col]:
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row+3, start_col:start_col+3]:
        return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row, col] = num
                        if solve_sudoku(board):
                            return True
                        board[row, col] = 0
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

if __name__ == "__main__":
    puzzle = np.array([
     [7, 0, 0, 4, 0, 0, 0, 8, 0],
     [0, 0, 3, 0, 0, 1, 0, 0, 5],
     [0, 2, 0, 0, 0, 0, 6, 0, 0],
     [8, 0, 0, 5, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 3, 0, 0, 0, 0],
     [0, 7, 0, 0, 0, 8, 0, 0, 6],
     [0, 0, 1, 0, 0, 0, 0, 2, 0],
     [2, 0, 0, 8, 0, 0, 7, 0, 0],
     [0, 4, 0, 0, 0, 6, 0, 0, 3]
    ])

    if solve_sudoku(puzzle):
        print("Solved Sudoku:")
        print_board(puzzle)
    else:
        print("No solution exists.")
