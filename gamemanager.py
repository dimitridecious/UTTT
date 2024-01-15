from masterboard import MasterBoard

class GameManager:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, screen):
        self.master_board = MasterBoard(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
         
    def draw_game(self):
        self.master_board.draw_master_grid()

    def get_hovered_cell(self,position):
        # find the cell that has x y position[0],position[1]
        pass
   
    def click(self, x, y):    
        if 0 <= int(y//(self.height/9)) < 9 and 0 <= int(x//(self.width/9)) < 9:
            print((int(y//(self.height/9)),int(x//(self.width/9))))
            return (int(y//(self.height/9)),int(x//(self.width/9)))
        else:
            return None