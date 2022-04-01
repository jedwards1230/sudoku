# sudoku

![Preview images](https://github.com/jedwards1230/sudoku/blob/master/screenshot.png)
A basic Django server that lets users play sudoku


## features
* board sizes ( 4x4 - 16x16 )
* difficulties ( 0 - 6 ) ( 0% hidden - 75% hidden )
* automatic dark mode


## to run
```
python manage.py runserver
```

## to do
* clearly display sub grids
* highlight values in same row, column, and sub grid
* fix formatting for large puzzles and small displays
* fix max request size limit for boards larger than 9x9 while checking solution
* format elapsed time to be readable
* use database to track average time per puzzle by size and difficulty
