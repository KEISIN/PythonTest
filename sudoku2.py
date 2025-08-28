def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku_bruteforce(board):
    empty_cells = [(row, col) for row in range(9) for col in range(9) if board[row][col] == 0]
    
    def solve(index):
        if index == len(empty_cells):
            return True
        row, col = empty_cells[index]
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                if solve(index + 1):
                    return True
                board[row][col] = 0
        return False
    
    return solve(0)

# 例：数独の初期状態（0は空のセル）
board=[
 [7, 0, 0, 4, 0, 0, 0, 8, 0],
 [0, 0, 3, 0, 0, 1, 0, 0, 5],
 [0, 2, 0, 0, 0, 0, 6, 0, 0],
 [8, 0, 0, 5, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 3, 0, 0, 0, 0],
 [0, 7, 0, 0, 0, 8, 0, 0, 6],
 [0, 0, 1, 0, 0, 0, 0, 2, 0],
 [2, 0, 0, 8, 0, 0, 7, 0, 0],
 [0, 4, 0, 0, 0, 6, 0, 0, 3]
]


if solve_sudoku_bruteforce(board):
    for row in board:
        print(row)
else:
    print("解が見つかりませんでした。")

