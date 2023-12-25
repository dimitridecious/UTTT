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
            self.surface = pygame.Surface((self.width, self.height),pygame.SRCALPHA)
            for i in range(1, 4):
                pygame.draw.line(self.surface, pygame.Color("black"), (i * self.width, 0), (i * self.width, self.height), 1)
                pygame.draw.line(self.surface, pygame.Color("black"), (0, i * self.height), (self.width, i * self.height), 1)

                        
    def print_grid(self):
        for i in self.grid:
            temp_array = []
            for j in i:
                temp_array.append(j.value)
            print(temp_array)

    def draw_grid(self, screen, posx, posy):
        screen.blit(self.surface,(posx,posy))


    