import random


def create_minesweeper_board(rows, cols, num_mines):
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        if board[row][col] != '*':
            board[row][col] = '*'
            mines_placed += 1

            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < rows and 0 <= j < cols and board[i][j] != '*':
                        board[i][j] += 1

    return board


if __name__ == '__main__':
    board = create_minesweeper_board(20, 20, 40)
    for row in board:
        print(row)
