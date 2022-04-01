from datetime import datetime
from django.shortcuts import render

import app.sudoku_utils as su


def index(request):
    context = {
        'config': {
            'size': 3,
            'difficulty': 0,
        },
    }
    
    if request.method == 'POST':
        context['config']['size'] = int(request.POST.get('size'))
        context['config']['difficulty'] = int(request.POST.get('difficulty'))
        
        # check submitted puzzle
        if request.POST.get('submit_puzzle') == '1':
            time = int(datetime.now().timestamp())
            start_time = int(request.POST.get('time')) or None
            delta_time = time - start_time
            puzzle, edits = su.to_python(request.POST)
            
            if puzzle and edits and delta_time:
                print('post', int(request.POST.get('time')))
                if su.check_solution(puzzle, context['config']['size']):
                    context['win'] = True
                    context['elapsed_time'] = str(delta_time)
                    print('elapsed', context['elapsed_time'])

                formset = su.new_formset(context['config']['size'], context['config']['difficulty'], puzzle, edits)
            else:
                context['invalid_submission'] = 'There was an error validating the board.'
        # generate new puzzle
        elif request.POST.get('new_puzzle') == '1':
            formset = su.new_formset(context['config']['size'], context['config']['difficulty'])
            context['time'] = int(datetime.now().timestamp())
            print('new', context['time'])
            
    else:
        formset = su.new_formset(context['config']['size'], context['config']['difficulty'])
        context['time'] = int(datetime.now().timestamp())
        print('init', context['time'])
    
    context['puzzle'] = formset
        
    return render(request, 'app/index.html', context)