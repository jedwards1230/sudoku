from math import sqrt


def print_grid(grid, label=None):
    if label:
        print('\n** ' + label + ' **\n')
    for row in grid:
        for x in row:
            if x == 0:
                print('_  ', end='')
            else:
                print(str(x) + '  ', end='')
        print()
    print()
    
def to_python(request):
    rows = []
    row = []
    
    # compute size of board
    side = 0
    for e in request:
        print(e)
        if 'col' in e:
            side += 1
    side = int(sqrt(side))
    
    # extract puzzle from request
    for i, k in enumerate(request):
        if 'col' in k:
            value = request.getlist(k)
            row.append(int(value[0]))
            
            # new row based on size
            if i % side == 0 and i > 0:
                rows.append(row)
                row = []
    
    return rows

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