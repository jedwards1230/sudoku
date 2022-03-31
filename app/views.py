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
            
            PuzzleFormSet = formset_factory(PuzzleForm)
            formset = PuzzleFormSet(initial=puzzle)
            
            context = {
                'puzzle': formset,
                'checked': True,
            }
            
            if formset.is_valid():
                context['win'] = win
    else:
        gen = SudokuGenerator(size=3, difficulty=0)
        puzzle, solution = gen.get_sudoku()
        puzzle = to_web(puzzle)
        
        PuzzleFormSet = formset_factory(PuzzleForm, max_num = len(puzzle))
        formset = PuzzleFormSet(initial = puzzle)
        
        context = {
            'puzzle': formset,
        }
        
    return render(request, 'app/index.html', context)