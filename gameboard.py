from cell import Cell
import pygame

class GameBoard:
    #no arguments needed, board will always be a blank 3x3 to start
    #TODO: initialize 2dimensional array of cells with 3row3col here
        #keep track of if game is ongoing/who winner is
    
        #later work on completed:bool
    def __init__(self, width, height, screen):
            self.width = width
            self.height = height
            self.screen = screen
            self.grid = []
            for i in range(3):
                temp_grid = []
                for j in range(3):
                    cell = Cell(width/3, height/3, False)
                    temp_grid.append(cell)
                self.grid.append(temp_grid)
                        
    def print_grid(self):
        for i in self.grid:
            temp_array = []
            for j in i:
                temp_array.append(j.value)
            print(temp_array)

    def draw_grid(self):
            self.screen.fill("white")
            block_width = self.width/3
            block_height = self.height/3
            line_width = 1
            for i in range(4):
                pygame.draw.line(self.screen, pygame.Color("black"), (0,i*block_width), (self.width, i*block_height),line_width)
                pygame.draw.line(self.screen, pygame.Color("black"), (i*block_width, 0), (i*block_width, self.height),line_width)

    