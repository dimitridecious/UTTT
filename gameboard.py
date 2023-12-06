from cell import Cell

class GameBoard:
    #no arguments needed, board will always be a blank 3x3 to start
    def __init__(self):
        #TODO: initialize 2dimensional array of cells with 3row3col here
        #keep track of if game is ongoing/who winner is
        self.winner = None

    #GameBoard methods go here