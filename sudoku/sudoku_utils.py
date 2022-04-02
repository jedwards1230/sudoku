import itertools
            

# check if puzzle is solved
def check_solution(board: list, size: int):
    def valid_line(line):
        line = set(line)
        try:
            line = [int(x) for x in line]
        except:
            raise ValueError(line, type(line))
        return (len(line) == side and sum(line) == sum(set(line)))
    
    # format board
    board = [row.split(',') for row in board]
    
    # check rows
    side = len(board)
    for row in board:
        for x in row:
            # check every value is int
            if not x.isdigit(): 
                return False
            # check value within proper range
            if not 0 < int(x) <= side: 
                return False
        # check values are unique
        if not valid_line(row): 
            return False
    
    # check cols
    board = list(zip(*board))
        
    for col in board:
        # check values are unique
        if not valid_line(col): 
            return False
    
    # check subgrids
    squares = []
    for i in range(0, side, size):
        for j in range(0, side, size):
            square = list(itertools.chain(row[j:j+size] for row in board[i:i+size]))
            squares.append(square)
    bad_squares = [square for line in square for square in squares if not valid_line(list(line))]
    if not bad_squares: 
        return False
            
    return True