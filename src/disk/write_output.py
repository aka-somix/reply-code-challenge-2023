def write_output(snakes, output_file_path):
    """
    Generate a text file with the layout of the given snakes.

    :param snakes: a list of tuples describing each snake
    :param output_file_path: the path of the output file to be created
    """
    with open(output_file_path, 'w') as f:
        for i, snake in enumerate(snakes):
            if snake is None:
                f.write('\n')
            else:
                c, r, direction, cw, rw = snake
                f.write(f"{c} {r} {direction} {cw} {rw}\n")
