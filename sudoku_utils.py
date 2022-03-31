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
        if len(row) != size:
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
    return True