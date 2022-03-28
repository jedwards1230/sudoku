from django.shortcuts import render
from .forms import PuzzleForm

from sudoku import SudokuGenerator

def index(request):
    if request.method == 'POST' and 'submit_puzzle' in request.POST:
        puzzle = SudokuGenerator().to_python(request.POST)
        puzzle = PuzzleForm(puzzle)
        context = {
            'puzzle': puzzle
        }
        
        if puzzle.is_valid():
            context['success'] = True
    else:
        gen = SudokuGenerator(size=3, difficulty=0)
        sudoku_puzzle = gen.to_web()
        puzzle = []
        
        for row in sudoku_puzzle:
            puzzle.append(PuzzleForm(initial=row))
        
        context = {
            'puzzle': puzzle,
        }
        
    return render(request, 'app/index.html', context)