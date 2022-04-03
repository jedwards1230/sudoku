from datetime import datetime
import json
from django.http import HttpResponse
from django.shortcuts import render
from sudoku.sudoku import SudokuGenerator
from sudoku.sudoku_utils import check_solution


def index(request):
    if request.method == 'POST':
        # check submitted puzzle
        if request.POST.get('submit_puzzle'):
            delta_time = int(datetime.now().timestamp()) - int(request.POST.get('time'))
            context = {
                'elapsed_time': str(delta_time),
            }
            
            puzzle = request.POST.getlist('puzzle[]')
            if puzzle:
                context['win'] = check_solution(puzzle, int(request.POST.get('size')))
                return HttpResponse(json.dumps(context), content_type="application/json")
            else:
                raise ValueError('Missing puzzle')
            
        # generate new puzzle
        elif request.POST.get('new_puzzle'):
            context = {
                'size': int(request.POST.get('size')),
                'difficulty': int(request.POST.get('difficulty')),
                'time': int(datetime.now().timestamp()),
            }
            context['puzzle'] = SudokuGenerator(context['size'], context['difficulty']).board_puzzle
            
            return HttpResponse(json.dumps(context), content_type="application/json")
            
    else:
        context = {
            'size': 2,
            'difficulty': 0,
            'time': int(datetime.now().timestamp()),
        }
        return render(request, 'sudoku/index.html', context)