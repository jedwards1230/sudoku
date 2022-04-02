// submit POST to check if puzzle is solved
function submit_puzzle() {
    console.log("submitting puzzle")
    size = $('#size').attr('value')
    difficulty = $('#difficulty').attr('value')
    create_time = $('#time').attr('value')
    csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value

    $.ajax({
        type: 'post',
        url: '',
        data: { 
            'submit_puzzle': true,
            'puzzle[]': get_puzzle(size),
            'csrfmiddlewaretoken': csrf_token,
            'size': size,
            'difficulty': difficulty,
            'time': create_time,
        },
        success: function(request) {
            console.log('puzzle checked');
            place_puzzle(request);
        },
    })
    return
}

// gather puzzle info from DOM
function get_puzzle(size) {
    console.log('gathering puzzle data from DOM')
    board_len = size * size
    count = 0
    puzzle = []
    row = ''
    $("#puzzle_form #grid input[type=number]").each(function(index) {
        row_i = index % board_len
        val = this.value;
        row += val
        if(row_i == board_len - 1 && index > 0) {
            count += 1;
            puzzle.push(row)
            row = ''
        }
    });

    return puzzle
}

// place puzzle into DOM
function place_puzzle(request) {
    console.log('placing puzzle')
    console.log(request);
    puzzle = request.puzzle;
    $('#time').val(request.time);
    $('#size').val(request.size);
    $('#difficulty').val(request.difficulty);

    if (request.win) {
        win = request.win;
        elapsed_time = request.elapsed_time;
        alert('Success! Seconds taken: ' + elapsed_time)
    }

    board_len = size * size;
    count = 0;
    puzzle_table = []
    for (i in puzzle) {
        puzzle_table.push('<tr>');
        for (j in puzzle[i]) {
            if (puzzle[i][j] == 0) {
                puzzle_table.push('<td><input type=\"number\" min=\"1\" max=\"' + board_len + '\" id=\"row-' + i + '-col-' + j + '\" required value=\"\"></td>\n')
            } else {
                puzzle_table.push('<td><input type=\"number\" min=\"1\" max=\"' + board_len + '\" id=\"row-' + i + '-col-' + j + '\" readonly value=\"' + puzzle[i][j] + '\" class=\"preset_value\"></td>\n')
            }
        }
        puzzle_table.push('</tr>')
    }
    $('#grid').empty();
    $('#grid').append( puzzle_table );
}

// request new puzzle with POST
function new_puzzle() {
    console.log("new puzzle requested")
    size = $('#size_select').find(":selected").attr('value');
    difficulty = $('#difficulty_select').find(":selected").attr('value');
    csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value

    console.log('size: ' + size + ' | difficulty: ' + difficulty)

    $.ajax({
        type: 'post',
        url: '',
        data: { 
            'new_puzzle': true,
            'csrfmiddlewaretoken': csrf_token,
            'size': size,
            'difficulty': difficulty,
        },
        success: function(request) {
            console.log('new puzzle received');
            place_puzzle(request);
        },
    })
    return
}

// prepare submit buttons
$(document).ready(function()
{
    $('#config_form').submit(function(event) {
        event.preventDefault();
        new_puzzle();
    });
    $('#puzzle_form').submit(function(event) {
        event.preventDefault();
        submit_puzzle();
    });
});