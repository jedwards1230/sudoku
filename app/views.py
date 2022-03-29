from django.shortcuts import render
from .forms import PuzzleForm

from sudoku import SudokuGenerator
from sudoku_utils import to_python, to_web

def index(request):
    if request.method == 'POST' and 'submit_puzzle' in request.POST:
        gen = SudokuGenerator()
        sudoku_puzzle = to_python(request.POST)
        
        # TODO: check if puzzle is solved
        # TODO: find out how to properly store original solution
        
        sudoku_puzzle = to_web(sudoku_puzzle)
        
        
        # TODO: Gotta figure out how to consolidate the rows for proper validation checking in django (or alt?)
        '''puzzle = []
        for row in sudoku_puzzle:
            puzzle.append(PuzzleForm(initial=row))'''
        
        puzzle = PuzzleForm({})
        
        context = {
            'puzzle': {puzzle}
        }
        
        if puzzle.is_valid():
            context['success'] = True
    else:
        gen = SudokuGenerator(size=3, difficulty=0)
        puzzle, solution = gen.get_sudoku()
        sudoku_puzzle = to_web(puzzle)
        
        puzzle = []
        for row in sudoku_puzzle:
            puzzle.append(PuzzleForm(initial=row))
        
        context = {
            'puzzle': puzzle,
        }
        
    return render(request, 'app/index.html', context)