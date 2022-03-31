import itertools
from math import sqrt


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
def to_python(request):
    rows = []
    row = []
    
    # compute size of board
    size = 0
    for e in request:
        if 'col' in e:
            size += 1
    side = int(sqrt(size))
    
    # extract puzzle from request
    for i, k in enumerate(request):
        if 'col' in k:
            value = request.getlist(k)
            if value[0]:
                row.append(int(value[0]))
            else:
                row.append(0)
            
            # new row based on size
            if i % side == 0 and i > 0:
                rows.append(row)
                row = []
                
    # check if board is malformed
    for row in rows:
        if len(row) != side:
            return None
    
    return rows

# convert sudoku board to be processed by Django formset_factory
def to_web(board):
    rows = []
    for row in board:
        id = 0
        puzzle = {}
        for val in row:
            n = 'col_' + str(id)
            puzzle[n] = val
            id += 1
        rows.append(puzzle)
    return rows

# TODO: check if puzzle is solved
def check_solution(board):
    def valid_line(line):
        return (len(line) == size and sum(line) == sum(set(line)))
    
    size = len(board)
    side = int(sqrt(size))
    
    # check rows
    for row in board:
        for x in row:
            # check every value is int
            if not isinstance(x, int): return False
            # check value within proper range
            if not 0 < x <= size: return False
        # check values are unique
        if not valid_line(row): return False
    
    # check cols
    board = list(zip(*board))
    for col in board:
        # check values are unique
        if not valid_line(col): return False
    
    # check subgrids
    squares = []
    for i in range(0, size, side):
        for j in range(0, size, side):
            square = list(itertools.chain(row[j:j+3] for row in board[i:i+3]))
            squares.append(square)
    bad_squares = [square for square in squares if not valid_line(square)]
    if not bad_squares: return False
            
    return True
    

            