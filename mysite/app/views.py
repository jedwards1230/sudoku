import json
from django.shortcuts import render


from sudoku import SudokuGenerator

def index(request):
    gen = SudokuGenerator(size=3, difficulty=4)
    sudoku_puzzle = gen.prepare_puzzle()
    
    context = {
        'sudoku_puzzle': sudoku_puzzle,
        
    }
    return render(request, 'app/index.html', context)

def check_puzzle(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        print('content', body_unicode)
        body = json.loads(body_unicode)
        content = body['content']
        print('content', content)

        return render(request, 'app/index.html')