def write_output(snakes, output_file_path):
    """
    Generate a text file with the layout of the given snakes.

    :param snakes: a list of tuples describing each snake
    :param output_file_path: the path of the output file to be created
    """
    with open(output_file_path, 'w') as f:
        for i, snake in enumerate(snakes):
            if snake.cells  != []:
                f.write(f"{snake.starting_cell[0]} {snake.starting_cell[1]} ")
                for j, move in enumerate(snake.moves):
                    if len(move) > 1:
                        f.write(f"{move[0]} {move[1]}")
                    else:
                        f.write(f"{move}")
                    if j != len(snake.moves) -1 :
                        f.write(" ")
            if i != len(snakes) -1 :
                f.write('\n')
