from django.shortcuts import render
from .forms import PuzzleForm

from sudoku import SudokuGenerator

def index(request):
    if request.method == 'POST' and 'submit_puzzle' in request.POST:
        form = PuzzleForm(request.POST)
        context = {
            'form': form
        }
        
        if form.is_valid():
            print(request.POST)
            context['success'] = True
        
        '''print(request.POST)
        
        context = {
            #'sudoku_puzzle': sudoku_puzzle,
        }'''

        return render(request, 'app/index.html', context)
    else:
        gen = SudokuGenerator(size=3, difficulty=0)
        
        # prepare data in Django form. tougher to iterate through to display row by row
        # may be easier to use without forms for easier iteration
        sudoku_puzzle = gen.prepare_puzzle_dict()
        form = PuzzleForm(initial=sudoku_puzzle)
        
        context = {
            'form': form,
        }
        
        # submits data as a list of lists (grid)
        # easier to display, but data changes (from str(value) to list(str(value))) so it may be cleaner to just use Django forms above
        # print request.POST and sudoku_puzzle to compare in/out data 
        '''sudoku_puzzle = gen.prepare_puzzle_list()
        context = {
            'sudoku_puzzle': sudoku_puzzle,
        }'''
        return render(request, 'app/index.html', context)