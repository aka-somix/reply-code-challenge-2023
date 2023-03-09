from game.snake import Snake
import random


def play_random(snakes, matrix):

    for snake in snakes:
        play_snake(snake)


def play_snake(snake: Snake, matrix):

    is_wh = True

    init_row = random.randint(0, len(matrix))
    init_col = random.randint(0, len(matrix[0]))

    while is_wh:
        cell = matrix[init_row][init_col]

        is_wh = cell.wh

    snake.starting_cell(init_row, init_col)

    while snake.snake_length > 0:
        direction = random.randint(0, 3)
