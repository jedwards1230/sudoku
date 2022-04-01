from django.shortcuts import render

import sudoku_utils as su


def index(request):
    context = {
        'config': {
            'size': 3,
            'difficulty': 4,
        }
    }
    
    if request.method == 'POST':
        context['config']['size'] = int(request.POST.get('size'))
        context['config']['difficulty'] = int(request.POST.get('difficulty'))
        
        # check submitted puzzle
        if request.POST.get('submit_puzzle') == '1':
            puzzle, edits = su.to_python(request.POST)
            
            if puzzle and edits:
                context['win'] = su.check_solution(puzzle, context['config']['size'])
                formset = su.new_formset(context['config']['size'], context['config']['difficulty'], puzzle, edits)
            else:
                context['invalid_submission'] = 'There was an error validating the board.'
        # generate new puzzle
        elif request.POST.get('new_puzzle') == '1':
            formset = su.new_formset(context['config']['size'], context['config']['difficulty'])
    else:
        formset = su.new_formset(context['config']['size'], context['config']['difficulty'])
    
    context['puzzle'] = formset
        
    return render(request, 'app/index.html', context)