from sys import argv

from disk.read_input import read_input
from disk.write_output import write_output

from strategies.helloworld import play_helloworld
from strategies.random_sg import play_random

from game.cell import Cell, Wormhole


class Game(object):

    def __init__(self, *, input, output):
        # Matrice del gioco (se ci sara)
        self.matrix: list(list(Cell | Wormhole)) = [[], []]
        self.snakes = []

        # Path dell'input
        self.input = input

        # Path dell'output
        self.output = output

    def write_solution(self):
        """
        TODO definisci l'input del metodo write output
        """
        self.matrix = write_output(self.snakes, self.output)

    def read_scenario(self):
        self.matrix, self.snakes = read_input(self.input)
        print(self.snakes)
        print('read input')
        # print(self.matrix)

    def play_scenario(self):
        """
        Swappa i metodi di gioco inserendo importando un metodo
        """
        play_random(self.snakes, self.matrix)


if __name__ == "__main__":

    # TAKE INPUT FROM ARGS
    INPUT, OUTPUT = argv[1:3]

    # Inizializza la classe game con il nome del file della soluzione
    game = Game(input=INPUT, output=OUTPUT)

    # Leggi l'input
    game.read_scenario()

    # Lancia il gioco
    game.play_scenario()

    # scrivi l'output
    game.write_solution()
