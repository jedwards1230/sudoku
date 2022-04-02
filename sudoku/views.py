from datetime import datetime
import json
from django.http import HttpResponse
from django.shortcuts import render

import sudoku.sudoku_utils as su


def index(request):
    context = {
        'size': 2,
        'difficulty': 1,
        'time': int(datetime.now().timestamp()),
    }
    
    if request.method == 'POST':
        context['size'] = int(request.POST.get('size'))
        context['difficulty'] = int(request.POST.get('difficulty'))
        
        # check submitted puzzle
        if request.POST.get('submit_puzzle'):
            puzzle = request.POST.getlist('puzzle[]')
            
            time = int(datetime.now().timestamp())
            context['time'] = int(request.POST.get('time'))
            delta_time = time - context['time']
            context['elapsed_time'] = str(delta_time)
            
            if puzzle:
                context['win'] = su.check_solution(puzzle, context['size'])
                context['puzzle'] = puzzle
                
                return HttpResponse(json.dumps(context), content_type="application/json")
            else:
                raise ValueError('Missing puzzle')
            
        # generate new puzzle
        elif request.POST.get('new_puzzle'):
            # TODO: large board get buggy
            context['puzzle'] = su.new_puzzle(context['size'], context['difficulty'])
            
            return HttpResponse(json.dumps(context), content_type="application/json")
            
    else:
        return render(request, 'sudoku/index.html', context)