import json
from django.shortcuts import render
from .forms import PuzzleForm

from sudoku import SudokuGenerator

def index(request):
    if request.method == 'POST' and 'submit_puzzle' in request.POST:
        solution = request.POST
        print(solution)
        
        form = PuzzleForm(request.POST)
        if form.is_valid():
            print(form)

        return render(request, 'app/index.html')
    else:
        gen = SudokuGenerator(size=3, difficulty=0)
        sudoku_puzzle = gen.prepare_puzzle()
        
        context = {
            'sudoku_puzzle': sudoku_puzzle,
            
        }
        return render(request, 'app/index.html', context)