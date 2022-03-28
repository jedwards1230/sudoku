import json
from django.shortcuts import render


from sudoku import SudokuGenerator

def index(request):
    gen = SudokuGenerator(size=3, difficulty=0)
    sudoku_puzzle = gen.prepare_puzzle()
    
    context = {
        'sudoku_puzzle': sudoku_puzzle,
        
    }
    return render(request, 'app/index.html', context)

def check_puzzle(request):
    if request.method == 'POST' and 'submit_puzzle' in request.POST:
        solution = request.POST
        print(solution)

        return render(request, 'app/index.html')