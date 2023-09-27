#sudoku puzzle create using python chatGPT
import random

def generate_solved_sudoku():
    base  = 3
    side  = base*base
    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(s): return random.sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    
    return board

def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def remove_numbers(board, difficulty_level):
    """
    Remove numbers from the solved Sudoku grid based on the difficulty level.
    """
    if difficulty_level == 'easy':
        num_to_remove = 30  # Easy: 30 numbers removed
    elif difficulty_level == 'medium':
        num_to_remove = 40  # Medium: 40 numbers removed
    else:
        num_to_remove = 50  # Hard: 50 numbers removed
    
    for _ in range(num_to_remove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0

# Generate a solved Sudoku puzzle
solved_sudoku = generate_solved_sudoku()

# Print the solved Sudoku puzzle
print("Solved Sudoku Puzzle:")
print_sudoku(solved_sudoku)

# Create a copy of the solved puzzle
unsolved_sudoku = [row[:] for row in solved_sudoku]

# Remove numbers to create a puzzle
difficulty_level = 'medium'  # Change difficulty level as needed ('easy', 'medium', 'hard')
remove_numbers(unsolved_sudoku, difficulty_level)

# Print the unsolved Sudoku puzzle (the generated puzzle)
print("\nUnsolved Sudoku Puzzle:")
print_sudoku(unsolved_sudoku)
