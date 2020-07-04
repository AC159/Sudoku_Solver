import time


def solve(board, row, col):
    # Base case, print the board and return True
    if row >= 9:
        for k in board:
            print(k)
        print("\n")
        return True

    if col >= 9:
        row += 1
        col = 0
        solve(board, row, col)
        return False

    # If column does not have a 0, just continue to the next column
    elif board[row][col] != 0:
        col += 1
        solve(board, row, col)
        return False

    else:
        for i in range(1, 10):

            if board[row][col] == 0:

                # Check if the placement is valid
                if presentInRow(board, row, i) or presentInColumn(board, col, i) or presentInSquare(board, row, col, i):
                    continue  # Try another integer i

                # If the number is correct, we update the board
                board[row][col] = i

                col += 1
                if solve(board, row, col):
                    return True

                # If a solution does not work, set the cell back to 0
                col -= 1
                board[row][col] = 0

        # Backtrack: no valid i integer could work with that sequence
        # Return to previous stack frame and try another integer i for the previous sequence of numbers
        # return False
        return False


# Function that takes the row number and the value to be found if present in that row
def presentInRow(board, rowNumber, i):
    for x in range(9):
        if board[rowNumber][x] == i:
            return True

    return False


# Function that takes the column number and the integer to look for
def presentInColumn(board, colNumber, i):
    for x in range(9):
        if board[x][colNumber] == i:
            return True

    return False


# Function that takes the row and column (to determine the square) in which we look the integer i if present
def presentInSquare(board, row, col, i):
    if 0 <= row < 3 and 0 <= col < 3:
        for x in range(3):
            for y in range(3):
                if board[x][y] == i:
                    return True
        return False

    elif 0 <= row < 3 and 3 <= col < 6:
        for x in range(3):
            for y in range(3, 6):
                if board[x][y] == i:
                    return True
        return False

    elif 0 <= row < 3 and 6 <= col < 9:
        for x in range(3):
            for y in range(6, 9):
                if board[x][y] == i:
                    return True
        return False

    elif 3 <= row < 6 and 0 <= col < 3:
        for x in range(3, 6):
            for y in range(0, 3):
                if board[x][y] == i:
                    return True
        return False

    elif 3 <= row < 6 and 3 <= col < 6:
        for x in range(3, 6):
            for y in range(3, 6):
                if board[x][y] == i:
                    return True
        return False

    elif 3 <= row < 6 and 6 <= col < 9:
        for x in range(3, 6):
            for y in range(6, 9):
                if board[x][y] == i:
                    return True
        return False

    elif 6 <= row < 9 and 0 <= col < 3:
        for x in range(6, 9):
            for y in range(0, 3):
                if board[x][y] == i:
                    return True
        return False

    elif 6 <= row < 9 and 3 <= col < 6:
        for x in range(6, 9):
            for y in range(3, 6):
                if board[x][y] == i:
                    return True
        return False

    elif 6 <= row < 9 and 6 <= col < 9:
        for x in range(6, 9):
            for y in range(6, 9):
                if board[x][y] == i:
                    return True
        return False


def main():
    # This board is represented row by row
    board1 = [

        [9, 0, 6, 0, 7, 0, 4, 0, 3],
        [0, 0, 0, 4, 0, 0, 2, 0, 0],
        [0, 7, 0, 0, 2, 3, 0, 1, 0],
        [5, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 4, 0, 2, 0, 8, 0, 6, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 5],
        [0, 3, 0, 7, 0, 0, 0, 5, 0],
        [0, 0, 7, 0, 0, 5, 0, 0, 0],
        [4, 0, 5, 0, 1, 0, 7, 0, 8],

    ]

    t1 = time.time()
    
    solve(board1, 0, 0)

    print("Execution time:", time.time() - t1, "seconds")


if __name__ == "__main__":
    main()
