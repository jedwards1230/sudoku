import itertools

from app.forms import PuzzleForm

from sudoku import SudokuGenerator


def print_grid(grid, label=None):
    if label:
        print('\n** ' + label + ' **\n')
    for row in grid:
        for x in row:
            if x == None:
                raise ValueError('Invalid cell input')
            if x == 0 or x == None:
                print('_  ', end='')
            else:
                print(str(x) + '  ', end='')
        print()
    print()

# convert sudoku board from POST request to list of lists
def to_python(request, size):
    board = []
    row = []
    edits_board = []
    edits_row = []
    
    i = 0
    
    l = size ** 2
    
    # extract puzzle from request
    for _, k in enumerate(request):
        if '_col_' in k:
            if request.get(k) == 'editable':
                edits_row.append(1)
            else:
                edits_row.append(0)
                
        if '-col_' in k:
            i += 1
            value = request.getlist(k)
            if value[0]:
                row.append(int(value[0]))
            else:
                row.append(0)
            
            # new row based on size
            if i % l == 0 and i > 0:
                board.append(row)
                edits_board.append(edits_row)
                row = []
                edits_row = []
                
    # check if board is malformed
    for row in board:
        if len(row) != l:
            return None
    
    return board, edits_board

# check if puzzle is solved
def check_solution(board, size):
    def valid_line(line):
        return (len(line) == side and sum(line) == sum(set(line)))
    
    side = len(board)
    
    # check rows
    for row in board:
        for x in row:
            # check every value is int
            if not isinstance(x, int): return False
            # check value within proper range
            if not 0 < x <= side: return False
        # check values are unique
        if not valid_line(row): return False
    
    # check cols
    board = list(zip(*board))
    for col in board:
        # check values are unique
        if not valid_line(col): return False
    
    # check subgrids
    squares = []
    for i in range(0, side, size):
        for j in range(0, side, size):
            square = list(itertools.chain(row[j:j+3] for row in board[i:i+3]))
            squares.append(square)
    bad_squares = [square for square in squares if not valid_line(square)]
    if not bad_squares: return False
            
    return True

def new_formset(size: int, difficulty: int, puzzle=None, edits=None):
    if not (puzzle and edits):
        gen = SudokuGenerator(size=size, difficulty=difficulty)
        puzzle, _ = gen.get_sudoku()
        
        edits = []
        for row in puzzle:
            r = []
            for i in row:
                if i == 0:
                    r.append(1)
                else:
                    r.append(0)
            edits.append(r)
    
    return PuzzleForm(puzzle, edits).get_formset()