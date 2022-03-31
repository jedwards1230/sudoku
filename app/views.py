from django.shortcuts import render

from sudoku import SudokuGenerator
from sudoku_utils import to_python, to_web, print_grid, check_solution, create_suduko_formset

def index(request):
    # TODO: is POST proper?
    if request.method == 'POST':
        puzzle = to_python(request.POST)
        if puzzle:
            win = check_solution(puzzle)
            
            puzzle = to_web(puzzle)
            
            # TODO: currently returns POST as readonly due to a value being in the form
            # Need to track modified values in request somehow
            
            context = {
                'puzzle': create_suduko_formset(puzzle),
                'win': win,
                'checked': True,
            }
        else:
            context = {
                'invalid_submission': 'There was an error validating the board.'
            }
    else:
        gen = SudokuGenerator(size=3, difficulty=0)
        puzzle, solution = gen.get_sudoku()
        puzzle = to_web(puzzle)
        
        context = {
            'puzzle': create_suduko_formset(puzzle),
        }
        
    return render(request, 'app/index.html', context)

def new_puzzle(request):
    return