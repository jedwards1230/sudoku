from django.shortcuts import render, redirect

import sudoku_utils as su


def index(request):
    context = {
        'config': {
            'size': 3,
            'difficulty': 0,
        }
    }
    # TODO: is POST proper?
    if request.method == 'POST':
        context['config']['size'] = int(request.POST.get('size'))
        context['config']['difficulty'] = int(request.POST.get('difficulty'))
        if request.POST.get('submit_puzzle') == '1':
            puzzle = su.to_python(request.POST, context['config']['size'])
            if puzzle:
                # TODO: currently returns POST as readonly due to a value being in the form
                # Need to track modified values in request somehow
                
                # TODO: formset generates extra form for some reason (10 rows instead of 9)
                
                context['win'] = su.check_solution(puzzle)
                formset = su.new_sudoku_formset(context['config']['size'], context['config']['difficulty'], puzzle)
            else:
                context = {
                    'invalid_submission': 'There was an error validating the board.'
                }
        if request.POST.get('new_puzzle') == '1':
            formset = su.new_sudoku_formset(context['config']['size'], context['config']['difficulty'])
    else:
        context['config']['size'] = 3
        context['config']['difficulty'] = 0
        
        formset = su.new_sudoku_formset(context['config']['size'], context['config']['difficulty'])
    
    context['size_desc'] = str(context['config']['size'] * context['config']['size']) + 'x' + str(context['config']['size'] * context['config']['size'])
    context['puzzle'] = formset
        
    return render(request, 'app/index.html', context)