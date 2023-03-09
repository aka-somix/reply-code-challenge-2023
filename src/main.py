from sys import argv

from disk.read_input import read_input
from disk.write_output import write_output

from strategies.helloworld import play_helloworld


class Game(object):

    def __init__(self, *, input, output):
        # Matrice del gioco (se ci sara)
        self.matrix = [[], []]

        # Path dell'input
        self.input = input

        # Path dell'output
        self.output = output

    def write_solution(self):
        """
        TODO definisci l'input del metodo write output
        """
        self.matrix = write_output(self.output)

    def read_scenario(self):
        """
        TODO definisci l'output del metodo write input
        """
        self.matrix = read_input(self.input)

    def play_scenario(self):
        """
        Swappa i metodi di gioco inserendo importando un metodo
        """
        play_helloworld()


if __name__ == "__main__":

    # TAKE INPUT FROM ARGS
    INPUT, OUTPUT = argv[1:3]

    # Inizializza la classe game con il nome del file della soluzione
    game = Game(input="test.txt", output="output_test.txt")

    # Leggi l'input
    game.read_scenario()

    # Lancia il gioco
    game.play_scenario()

    # scrivi l'output
    game.write_solution()
