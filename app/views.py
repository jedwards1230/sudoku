from django.shortcuts import render
from .forms import PuzzleForm

from sudoku import SudokuGenerator

def index(request):
    if request.method == 'POST' and 'submit_puzzle' in request.POST:
        #print(request.POST)
        form = PuzzleForm(request.POST)
        context = {
            'form': form
        }
        
        if form.is_valid():
            print(request.POST)
        
        '''print(request.POST)
        
        context = {
            #'sudoku_puzzle': sudoku_puzzle,
        }'''

        return render(request, 'app/index.html', context)
    else:
        gen = SudokuGenerator(size=3, difficulty=0)
        
        sudoku_puzzle = gen.prepare_puzzle_dict()
        form = PuzzleForm(initial=sudoku_puzzle)
        
        context = {
            'form': form,
        }
        
        '''sudoku_puzzle = gen.prepare_puzzle_list()
        sudoku_puzzle1 = gen.prepare_puzzle_dict()
        #print(sudoku_puzzle1)
        context = {
            'sudoku_puzzle': sudoku_puzzle,
        }'''
        return render(request, 'app/index.html', context)