from gamemanager import GameManager
from masterboard import MasterBoard
from gameboard import GameBoard
import pygame

#system variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

#game objects
#TODO:make a masterboard instance and gamemanager instance
#TODO:give the game manager the masterboard to manage
#TODO:use the gamemanager to perform manipulations to the masterboard in main gameloop!

#pygame gameloop 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    my_gameboard = GameBoard(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    my_gameboard.print_grid()

    while running:

        my_gameboard.draw_grid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()