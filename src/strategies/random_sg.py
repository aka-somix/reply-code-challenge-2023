from game.snake import Snake
import random


def play_random(snakes, matrix):

    for snake in snakes:
        play_snake(snake, matrix)


def play_snake(snake: Snake, matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])

    print(f"{nrows}|{ncols}")

    is_wh = True

    init_row = random.randint(0, nrows - 1)
    init_col = random.randint(0, ncols - 1)

    while is_wh:
        print(f"{init_row}|{init_col}")
        cell = matrix[init_row][init_col]

        is_wh = cell.wh

    snake.starting_cell = (init_row, init_col)

    cur_row = init_row
    cur_col = init_col

    while snake.snake_length > 0:

        directions = ["U", "R", "D", "L"]
        random.shuffle(directions)

        # Scegli ad esclusione randomica la prossima posizione
        cur_cell = matrix[cur_row][cur_col]
        next_pos = (-1, -1)
        next_dir = "-"

        for d in directions:
            if d == "U":
                next_pos = cur_cell.up()

            elif d == "R":
                next_pos = cur_cell.right()

            elif d == "D":
                next_pos = cur_cell.down()

            elif d == "L":
                next_pos = cur_cell.left()

            print(f"next pos: {next_pos}")

            next_pos = (next_pos[0][0], next_pos[0][1])

            next_cell = matrix[next_pos[0]][next_pos[1]]

            if next_cell.wh or next_cell.free:
                break

        if next_cell.row < 0 and next_cell.col < 0:
            # TODO RESET SNAKE
            continue

        print(snake.cells)

        snake.move_snake(next_dir, next_cell)
        cur_row = next_pos[0]
        cur_col = next_pos[1]

        if not next_cell.wh:
            next_cell.free = False
