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

    def draw_master_grid(self):
            self.screen.fill("white")
            block_width = self.width/3
            block_height = self.height/3
            line_width = 3
            for i in range(4):
                pygame.draw.line(self.screen, pygame.Color("black"), (0,i*block_width), (self.width, i*block_height),line_width)
                pygame.draw.line(self.screen, pygame.Color("black"), (i*block_width, 0), (i*block_width, self.height),line_width)

            #placing gameboards into master grid    
            grid_placement = [0, 0]
            for i in self.master_grid:
                for j in i:
                    j.draw_grid(self.screen,grid_placement[0], grid_placement[1])
                    grid_placement[0]+= block_width
                grid_placement[0] = 0    
                grid_placement[1]+= block_height
                    
                