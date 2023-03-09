"""
prendo i serpenti in ordine di grandezza e li posiziono sulle celle libere con valore più grande, spostandolo sempre verso la cella più grande
"""
from game.snake import Snake
from game.cell import Cell, Wormhole


def play_strategy_three(matrix:list(list), snakes: list(Snake)):
    total_cells=matrix[0][0].nrows*matrix[0][0].ncols
    total_snake_lengths=sum([s.snake_length for s in snakes])

    all_cells=[cell for cell in (row for row in matrix)]

    # ordino le celle per grandezza ascendente
    all_cells.sort(key=lambda x: x.value, reverse=True)

    # ordino i serpenti per grandezza discendente

    snakes.sort(key=lambda x: x.snake_length, reverse=True)
    
    # ciclo su tutti i serpenti
    for s in snakes:
    # ciclo sulla lunghezza del serpente
        for i in range(s.snake_length):
        # se è il primo indice del serpente che inserisco
            if i == 0:
                s.set_starting_cell(all_cells[0])
                all_cells.pop(0)
            # cerco una cella libera dal massimo valore nella matrice
            # posiziono la cella del serpente
        # dal 2 indice alla fine sel serpente
            # dalla cella trovata guardo le celle che ho attorno e prendo quella libera da valore max
            # posiziono la seconda cella del serpente

