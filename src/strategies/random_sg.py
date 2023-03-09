from game.snake import Snake
import random


def play_random(snakes, matrix):

    print(f"SNAKES {snakes}")

    for s in snakes:
        print(f"-------------------- {s} -------------------------------")
        print(s.moves)
        play_snake(s, matrix)


def play_snake(snake: Snake, matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])

    init_row = random.randint(0, nrows - 1)
    init_col = random.randint(0, ncols - 1)
    is_wh = True

    print("CHOOSING STARTING POSITION")

    while is_wh:
        init_row = random.randint(0, nrows - 1)
        init_col = random.randint(0, ncols - 1)
        cell = matrix[init_row][init_col]
        is_wh = cell.wh

    snake.starting_cell = (init_row, init_col)

    cur_row = init_row
    cur_col = init_col

    print("MOVING!")

    for iter in range(snake.snake_length):

        print(f"ITERATION: {iter}")

        directions = ["U", "R", "D", "L"]
        random.shuffle(directions)

        # Scegli ad esclusione randomica la prossima posizione
        cur_cell = matrix[cur_row][cur_col]
        next_pos = (-1, -1)
        next_dir = "-"

        for d in directions:
            if d == "U":
                next_pos = cur_cell.up()
                next_dir = "U"
            elif d == "R":
                next_pos = cur_cell.right()
                next_dir = "R"
            elif d == "D":
                next_pos = cur_cell.down()
                next_dir = "D"
            elif d == "L":
                next_pos = cur_cell.left()
                next_dir = "L"

            next_pos = (next_pos[0][0], next_pos[0][1])

            next_cell = matrix[next_pos[0]][next_pos[1]]

            if next_cell.wh or next_cell.free:
                break

        if next_cell.row < 0 and next_cell.col < 0:
            # TODO RESET SNAKE
            return

        print(snake.moves)

        snake.move_snake(next_dir, next_cell)

        print(snake.moves)

        cur_row = next_pos[0]
        cur_col = next_pos[1]

        if not next_cell.wh:
            next_cell.free = False
