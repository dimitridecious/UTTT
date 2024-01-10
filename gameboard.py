from cell import Cell
import pygame

class GameBoard:
    #no arguments needed, board will always be a blank 3x3 to start
    #TODO: initialize 2dimensional array of cells with 3row3col here
        #keep track of if game is ongoing/who winner is
    
        #later work on completed:bool
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        for i in range(3):
            temp_grid = []
            for j in range(3):
                cell = Cell(width/3, height/3, False)
                temp_grid.append(cell)
            self.grid.append(temp_grid)

        # Create surfaces for each sub-board
        self.surface = pygame.Surface([width, height])

    def print_grid(self):
        for i in self.grid:
            temp_array = []
            for j in i:
                temp_array.append(j.value)
            print(temp_array)

    def draw_board(self, posx, posy, master_surface):
        self.surface.fill("white")
        block_width = self.width/3
        block_height = self.height/3
        line_width = 1
        # populate with cells
        self.draw_cells()
        # draw gameboard lines
        for i in range(4):
            pygame.draw.line(self.surface, pygame.Color("black"), (0,i*block_width), (self.width, i*block_height),line_width)
            pygame.draw.line(self.surface, pygame.Color("black"), (i*block_width, 0), (i*block_width, self.height),line_width)
        # draw gameboard onto masterboard
        master_surface.blit(self.surface, (posx, posy))

    def draw_cells(self):
        block_width = self.width/3
        block_height = self.height/3
        x_pos = 0
        y_pos = 0
        for row in self.grid:
            if x_pos == block_width * 3:
                y_pos += block_height
            x_pos = 0
            for cell in row:
                cell.draw_cell(x_pos, y_pos, self.surface)
                x_pos += block_width