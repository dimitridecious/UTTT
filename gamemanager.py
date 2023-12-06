from masterboard import MasterBoard

class GameManager:
    def __init__(self, master_board, to_go_first):
        self.master_board = master_board
        #does X or O get to go first? decided in main for now.
        self.to_go_first = to_go_first
        #in play or over - who won?
        self.grand_winner = None
    
    #GameManager methods go here