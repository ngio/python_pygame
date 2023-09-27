# sudoku puzzle create using python chatGPT

import random
import copy

def generate_sudoku():
    base  = 3
    side  = base*base

    # Pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # Randomly shuffle rows, columns and numbers (of valid base pattern)
    def shuffle(s): return random.sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # Produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    return board

def remove_numbers(board, num_to_remove):
    puzzle = copy.deepcopy(board)
    for _ in range(num_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0
    return puzzle

def print_sudoku(board):
    for row in board:
        print(' '.join(str(num) if num != 0 else '.' for num in row))

# Generate a Sudoku solution
solution = generate_sudoku()

# Print the solution
print("Sudoku Solution:")
print_sudoku(solution)

# Create a puzzle by removing some numbers
num_to_remove = 30  # Adjust the number of removed numbers as desired
puzzle = remove_numbers(solution, num_to_remove)

# Print the Sudoku puzzle
print("\nSudoku Puzzle:")
print_sudoku(puzzle)
