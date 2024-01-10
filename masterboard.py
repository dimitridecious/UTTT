from gameboard import GameBoard
import pygame

#something to think about:
#each gameboard is technically just a Cell in the eyes of the master gameboard, right??

class MasterBoard:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.master_grid = []
        for i in range(3):
            temp_grid = []
            for j in range(3):
                gameboard = GameBoard(width/3, height/3)
                temp_grid.append(gameboard)
            self.master_grid.append(temp_grid)
        self.surface = pygame.Surface([width, height])

    def draw_master_grid(self):
        self.surface.fill("white")
        block_width = self.width/3
        block_height = self.height/3
        line_width = 5

        #populate with boards
        self.draw_gameboards()
        #draw master lines
        for i in range(4):
            pygame.draw.line(self.surface, pygame.Color("black"), (0,i*block_width), (self.width, i*block_height),line_width)
            pygame.draw.line(self.surface, pygame.Color("black"), (i*block_width, 0), (i*block_width, self.height),line_width)
        
        #draw master board onto screen
        self.screen.blit(self.surface, (0, 0))
                
    def draw_gameboards(self):
        block_width = self.width/3
        block_height = self.height/3
        x_pos = 0
        y_pos = 0
        for row in self.master_grid:
            if x_pos == block_width * 3:
                y_pos += block_height
            x_pos = 0
            for board in row:
                board.draw_board(x_pos, y_pos, self.surface)
                x_pos += block_width
