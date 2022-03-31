from django.forms import formset_factory
from django.shortcuts import redirect, render
from .forms import PuzzleForm

from sudoku import SudokuGenerator
from sudoku_utils import to_python, to_web, print_grid, check_solution

def index(request):
    if request.method == 'POST':
        puzzle = to_python(request.POST)
        if puzzle:
            win = check_solution(puzzle)
            
            puzzle = to_web(puzzle)
            
            # TODO: currently returns POST as readonly due to a value being in the form
            # Need to track modified values in request somehow
            
            PuzzleFormSet = formset_factory(PuzzleForm)
            formset = PuzzleFormSet(initial=puzzle, auto_id=False)
            
            context = {
                'puzzle': formset,
                'win': win,
                'checked': True,
            }
        else:
            context = {
                'invalid_submission': 'There was an error validating the board.'
            }
    else:
        gen = SudokuGenerator(size=3, difficulty=1)
        puzzle, solution = gen.get_sudoku()
        puzzle = to_web(puzzle)
        
        PuzzleFormSet = formset_factory(PuzzleForm, max_num = len(puzzle))
        formset = PuzzleFormSet(initial = puzzle, auto_id=False)
        
        context = {
            'puzzle': formset,
        }
        
    return render(request, 'app/index.html', context)