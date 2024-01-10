import pygame
class Cell:
    #constructor for cell class, has a value (string) and occupied status (bool)
    def __init__(self, width, height, occupied:bool, value:str = ''):
        self.width = width
        self.height = height
        self.value = value
        self.occupied = occupied
        self.surface = pygame.Surface([width, height])
    
    def draw_cell(self, posx, posy, gameboard_surface):
        font = pygame.font.Font("./assets/BruceForeverRegular-X3jd2.ttf", 90)
        self.surface.fill("white")
        value_surface = font.render(self.value, True, "blue")
        self.surface.blit(value_surface, (11, 0))
        gameboard_surface.blit(self.surface, (posx, posy))