// submit POST to check if puzzle is solved
// displays alert
function submit_puzzle() {
    console.log("Submitting puzzle for evaluation");
    size = $('#size').attr('value');
    difficulty = $('#difficulty').attr('value');
    create_time = $('#time').attr('value');
    csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

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
        success: function (request) {
            console.log('Puzzle evaluated');
            success_alert(request.win, request.elapsed_time);
        },
    })
    return
}

// display alert for win/loss
function success_alert(win, time) {
    // clear any success notifications
    $('#success').empty()

    if (win == true) {
        console.log('Puzzle solved!')
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
        console.log('Invalid puzzle submission!')
        $('#success').append(
            $('<div/>', {
                'class': 'alert alert-danger mx-auto',
                'role': 'alert'
            }).append(
                $('<h4/>', {
                    'class': 'alert-heading',
                    text: 'Try again'
                })
            ).append(
                $('<p/>', {
                    'class': 'mb-0',
                    text: 'Time taken: ' + time
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
function get_puzzle(size) {
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
            place_puzzle(request);
        },
    })
    return
}

// prepare submit buttons
$(document).ready(function () {
    $('#config_form').submit(function (event) {
        event.preventDefault();
        new_puzzle();
    });
    $('#puzzle_form').submit(function (event) {
        event.preventDefault();
        submit_puzzle();
    });
});