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
    # extract puzzle from request
    cols = []
    for key, _ in request.items():
        if 'col' in key:
            value = request.getlist(key)
            cols.append(value)
    
    # transpose cols x rows and convert to int lists
    cols = zip(*cols)
    cols = [[int(item) for item in col] for col in cols]
    
    return cols

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