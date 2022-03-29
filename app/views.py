from django.forms import formset_factory
from django.shortcuts import render
from .forms import PuzzleForm

from sudoku import SudokuGenerator
from sudoku_utils import to_python, to_web, print_grid, check_solution

def index(request):
    PuzzleFormSet = formset_factory(PuzzleForm)
    
    if request.method == 'POST' and 'submit_puzzle' in request.POST:
        sudoku_puzzle = to_python(request.POST)
        
        win = check_solution(sudoku_puzzle)
        
        sudoku_puzzle = to_web(sudoku_puzzle)
        formset = PuzzleFormSet(initial=sudoku_puzzle)
        
        context = {
            'puzzle': formset,
        }
        
        if formset.is_valid():
            context['success'] = win
    else:
        gen = SudokuGenerator(size=3, difficulty=0)
        puzzle, solution = gen.get_sudoku()
        sudoku_puzzle = to_web(puzzle)
        
        formset = PuzzleFormSet(initial=sudoku_puzzle)
        
        context = {
            'puzzle': formset,
        }
        
    return render(request, 'app/index.html', context)