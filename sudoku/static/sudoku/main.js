// submit POST to check if puzzle is solved
// displays alert
function submit_puzzle(puzzle) {
    size = $('#size').attr('value');
    difficulty = $('#difficulty').attr('value');
    create_time = $('#time').attr('value');
    csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    $.ajax({
        type: 'post',
        url: '',
        data: {
            'submit_puzzle': true,
            'puzzle[]': puzzle,
            'csrfmiddlewaretoken': csrf_token,
            'size': size,
            'difficulty': difficulty,
            'time': create_time,
        },
        success: function (request) {
            console.log('Puzzle submitted');
            console.log(request);
            success_alert(true, request.elapsed_time);
        },
    })
    return
}

// display alert for win/loss
function success_alert(win, time) {
    // clear any success notifications
    $('#success').empty()

    if (win == true) {
        $('#success').append(
            $('<div/>', {
                'class': 'alert alert-success mx-auto',
                'role': 'alert'
            }).append(
                $('<h4/>', {
                    'class': 'alert-heading',
                    text: 'You win!'
                })
            ).append(
                $('<p/>', {
                    'class': 'mb-0',
                    text: 'Time taken: ' + time
                })
            )
        );
    } else if (win == false) {
        $('#success').append(
            $('<div/>', {
                'class': 'alert alert-danger mx-auto',
                'role': 'alert'
            }).append(
                $('<h4/>', {
                    'class': 'alert-heading',
                    text: 'Try again'
                })
            )
        );
    }

    // clear alert on click
    $('#success').click(function () {
        $('#success').empty();
    });
}

// gather puzzle info from DOM
// returns puzzle as array
function get_puzzle() {
    size = $('#size').attr('value');
    board_len = size * size;
    count = 0;
    puzzle = [];
    row = [];
    $("#puzzle_form #grid input[type=number]").each(function (index) {
        row_i = index % board_len;
        row.push(this.value);
        if (row_i == board_len - 1 && index > 0) {
            count += 1;
            puzzle.push(row);
            row = [];
        }
    });

    return puzzle
}

// place puzzle into DOM
function place_puzzle(request) {
    console.log('Arranging puzzle');
    puzzle = request.puzzle;
    $('#time').val(request.time);
    $('#size').val(request.size);
    $('#difficulty').val(request.difficulty);

    board_len = size * size;
    count = 0;
    $('#grid').empty();
    for (i in puzzle) {
        $('#grid').append('<tr/>');
        for (j in puzzle[i]) {
            // if value is 0, set a blank spot
            if (puzzle[i][j] == 0) {
                $('#grid').append(
                    $('<td/>').append(
                        $('<input/>', {
                            'type': 'number',
                            'min': '1',
                            'max': board_len,
                            'id': 'row-' + i + '-col-' + j,
                            required: true,
                            'value': ''
                        })
                    ).append(
                        $('<label/>', {
                            'for': 'row-' + i + '-col-' + j,
                            'value': '',
                        })
                    )
                );
                // else display actual value
            } else {
                $('#grid').append(
                    $('<td/>').append(
                        $('<input/>', {
                            'type': 'number',
                            'min': '1',
                            'max': board_len,
                            'id': 'row-' + i + '-col-' + j,
                            readonly: true,
                            'value': puzzle[i][j],
                            'class': 'preset_value'
                        })
                    ).append(
                        $('<label/>', {
                            'for': 'row-' + i + '-col-' + j,
                            'value': puzzle[i][j],
                        })
                    )
                );
            }
        }
    }
    console.log('Puzzle ready!');
}

// request new puzzle with POST
function new_puzzle() {
    // clear any success notifications
    $('#success').empty();
    size = $('#size_select').find(":selected").attr('value');
    difficulty = $('#difficulty_select').find(":selected").attr('value');
    csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value

    console.log('New puzzle request: (size : ' + size + ') (difficulty : ' + difficulty + ')');

    $.ajax({
        type: 'post',
        url: '',
        data: {
            'new_puzzle': true,
            'csrfmiddlewaretoken': csrf_token,
            'size': size,
            'difficulty': difficulty,
        },
        success: function (request) {
            console.log('New puzzle received');
            console.log(request);
            place_puzzle(request);
        },
    })
    return
}

function check_puzzle() {
    function check_line(line) {
        sum1 = line.reduce((a, b) => a + b, 0);
        set = new Set(line)
        sum2 = [...set].reduce((a, b) => a + b, 0);
        return (line.length == side && sum1 == sum2)
    }

    puzzle_complete = get_puzzle();
    puzzle = [...puzzle_complete]
    side = puzzle.length;
    size = $('#size').attr('value');

    for (i in puzzle) {
        for (j in puzzle[i]) {
            // checks if number
            if (isNaN(puzzle[i][j]) && isNaN(parseFloat(puzzle[i][j]))) {
                return success_alert(false);
            }
            // checks for within range
            if (!(0 < puzzle[i][j] <= side)) {
                return success_alert(false);
            }
        }
        // check rows are valid
        if (!check_line(puzzle[i])) {
            return success_alert(false);
        }
    }

    // transpose board
    puzzle = puzzle[0].map((_, colIndex) => puzzle.map(row => row[colIndex]));

    // check columns are valid
    for (i in puzzle) {
        if (!check_line(puzzle[i])) {
            return success_alert(false);
        }
    }

    // TODO: check subgrids
    /* 
    squares = []
    for i in range(0, side, size):
        for j in range(0, side, size):
            square = list(itertools.chain(row[j:j+size] for row in board[i:i+size]))
            squares.append(square)
    bad_squares = [square for line in square for square in squares if not valid_line(list(line))]
    if not bad_squares: 
        return False
    */

    console.log('Puzzle solved!')
    submit_puzzle(puzzle_complete);

}

// prepare submit buttons
$(document).ready(function () {
    $('#config_form').submit(function (event) {
        event.preventDefault();
        new_puzzle();
    });
    $('#puzzle_form').submit(function (event) {
        event.preventDefault();
        check_puzzle();
    });
});