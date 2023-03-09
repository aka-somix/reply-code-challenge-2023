"""
prendo i serpenti in ordine di grandezza e li posiziono sulle celle libere con valore più grande, spostandolo sempre verso la cella più grande
"""
from game.snake import Snake
from game.cell import Cell, Wormhole
from itertools import chain


def play_strategy_three(matrix , snakes):
    # total_cells=matrix[0][0].nrows*matrix[0][0].ncols
    # total_snake_lengths=sum([s.snake_length for s in snakes])

    all_cells = list(chain.from_iterable(matrix))

    # ordino le celle per grandezza ascendente
    all_cells.sort(key=lambda x: x.value, reverse=True)
    print(all_cells)

    # ordino i serpenti per grandezza discendente

    snakes.sort(key=lambda x: x.snake_length, reverse=True)
    
    # ciclo su tutti i serpenti
    for s in snakes:
        skip_snake=False
        # ciclo sulla lunghezza del serpente
        for i in range(s.snake_length):
            # se è il primo indice del serpente che inserisco
            if i == 0:
                # cerco una cella libera dal massimo valore nella matrice
                # posiziono la cella del serpente
                s.set_starting_cell(all_cells[0])
                all_cells.pop(0)
            # dal 2 indice alla fine sel serpente
            else:                
                # dalla cella trovata guardo le celle che ho attorno e prendo quella libera da valore max
                    current_cell=s.cells[-1]
                    tmp=[
                        [('L', matrix[x][y]) for (x, y) in current_cell.left()],
                        [('R', matrix[x][y]) for (x, y) in current_cell.right()],
                        [('U', matrix[x][y]) for (x, y) in current_cell.up()],
                        [('D', matrix[x][y]) for (x, y) in current_cell.down()],
                    ]
                    adjacent_cells = list(chain.from_iterable(tmp))
                    adjacent_cells.sort(key= lambda x: x[1].value if x[1].free else -1, reverse=True)
                    if adjacent_cells[0][1].free:
                        s.move_snake(adjacent_cells[0][0], adjacent_cells[0][1])
                    else:
                        skip_snake=True
                        for cell in s.cells:
                            cell.free = True
                        s.cells=[]
                        s.moves=[]
                        s.starting_cell=[]
                        continue
                # posiziono la seconda cella del serpente
        if skip_snake:
            continue

